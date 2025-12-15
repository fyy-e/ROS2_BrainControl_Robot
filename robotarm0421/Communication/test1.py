import serial
import time
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from action_msgs.msg import GoalStatus

# --------------------------
# 基础配置
# --------------------------
# 串口配置
serial1_port = '/dev/ttyCH341USB0'
serial1_baudrate = 115200
serial2_port = '/dev/ttyCH341USB1'
serial2_baudrate = 9600

# 帧头帧尾
FRAME_HEADER = b'\x7B'
FRAME_FOOTER = b'\x7D'

# 指令映射
command_mapping = {
    b'5': ('关灯', '关闭所有灯光'),
    b'2': ('开灯', '打开所有灯光'),
    b'3': ('送水', ''),
    b'4': ('送药', ''),
    b'1': ('开门', '打开大门'),
    b'6': ('报警', '启动报警系统')
}

# 导航目标
water_x, water_y, water_yaw = 1.8, -0.5, -1.57
medicine_x, medicine_y, medicine_yaw = 1.8, 0.8, 1.57

# 状态变量
system_state = {
    'light': "关闭",
    'water_delivery': "未送",
    'medicine_delivery': "未送",
    'door': "关闭",
    'alarm': "未报警",
    'navigation': "idle"  # idle/navigating/completed/failed
}


# --------------------------
# ROS2导航节点（修复状态更新）
# --------------------------
class NavigationNode(Node):
    def __init__(self):
        super().__init__('navigation_controller')
        self.nav_publisher = self.create_publisher(PoseStamped, 'goal_pose', 10)
        self.status_sub = self.create_subscription(
            GoalStatus,
            '/goal_status',
            self.status_callback,
            10
        )
        self.current_goal_status = GoalStatus.STATUS_SUCCEEDED
        self.get_logger().info('ROS2导航节点已启动')

    def status_callback(self, msg):
        """增强状态更新日志，确保状态正确同步"""
        prev_status = self.current_goal_status
        self.current_goal_status = msg.status
        
        # 打印状态变化（方便调试）
        status_map = {
            GoalStatus.STATUS_SUCCEEDED: "成功",
            GoalStatus.STATUS_ACTIVE: "活跃",
            GoalStatus.STATUS_ABORTED: "失败",
            GoalStatus.STATUS_CANCELED: "取消"
        }
        self.get_logger().info(
            f"导航状态变化: {status_map.get(prev_status, '未知')} → {status_map.get(self.current_goal_status, '未知')}"
        )
        
        # 强制更新系统状态
        if self.current_goal_status == GoalStatus.STATUS_ACTIVE:
            system_state['navigation'] = "navigating"
        elif self.current_goal_status == GoalStatus.STATUS_SUCCEEDED:
            system_state['navigation'] = "completed"
        elif self.current_goal_status in [GoalStatus.STATUS_ABORTED, GoalStatus.STATUS_CANCELED]:
            system_state['navigation'] = "failed"

    def send_goal(self, x, y, yaw):
        goal_msg = PoseStamped()
        goal_msg.header.frame_id = 'map'
        goal_msg.header.stamp = self.get_clock().now().to_msg()
        goal_msg.pose.position.x = x
        goal_msg.pose.position.y = y
        goal_msg.pose.position.z = 0.0
        
        import math
        goal_msg.pose.orientation.z = math.sin(yaw / 2.0)
        goal_msg.pose.orientation.w = math.cos(yaw / 2.0)
        
        self.nav_publisher.publish(goal_msg)
        self.get_logger().info(f'已发送导航目标：x={x}, y={y}')
        system_state['navigation'] = "navigating"
        return True

    def wait_for_completion(self, timeout=30):
        """修复：确保导航完成后状态强制更新"""
        start_time = time.time()
        while rclpy.ok():
            # 每0.5秒打印一次当前状态（调试用）
            if int(time.time() - start_time) % 5 == 0:
                self.get_logger().info(f"等待导航完成...当前状态: {system_state['navigation']}")
            
            if system_state['navigation'] == "completed":
                # 强制重置状态为idle（关键修复）
                system_state['navigation'] = "idle"
                self.get_logger().info("导航完成，状态重置为空闲")
                return True
            if system_state['navigation'] == "failed":
                system_state['navigation'] = "idle"
                self.get_logger().info("导航失败，状态重置为空闲")
                return False
            if time.time() - start_time > timeout:
                self.get_logger().warn("导航超时，强制重置状态")
                system_state['navigation'] = "idle"  # 超时后强制重置
                return False
            
            rclpy.spin_once(self, timeout_sec=0.1)
            time.sleep(0.1)


# --------------------------
# 串口通信类（增加缓存清理）
# --------------------------
class SerialCommunication:
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.ser = None

    def open(self):
        try:
            if self.ser and self.ser.is_open:
                self.close()
            self.ser = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=1.0
            )
            if self.ser.is_open:
                print(f"串口 {self.port} 已打开")
                return True
            return False
        except Exception as e:
            print(f"打开串口 {self.port} 失败: {e}")
            return False

    def close(self):
        if self.ser and self.ser.is_open:
            self.ser.close()
            print(f"串口 {self.port} 已关闭")

    def send_with_frame(self, text):
        if not self.ser or not self.ser.is_open:
            print("串口未打开，无法发送")
            return False
        try:
            text_bytes = text.encode('utf-8')
            frame = FRAME_HEADER + text_bytes + FRAME_FOOTER
            self.ser.write(frame)
            print(f"串口1发送: {frame.hex()} （内容：{text}）")
            return True
        except Exception as e:
            print(f"串口1发送失败: {e}")
            return False

    def receive_bytes(self):
        """修复：读取后清空缓存，避免重复接收同一指令"""
        if not self.ser or not self.ser.is_open:
            return None
        try:
            data = self.ser.read(1)
            # 关键修复：如果有剩余数据，清空缓存（防止重复读取）
            if self.ser.in_waiting > 0:
                self.ser.read(self.ser.in_waiting)
            return data if data else None
        except Exception as e:
            print(f"串口2接收失败: {e}")
            return None


# --------------------------
# 命令处理函数
# --------------------------
def handle_normal_command(received_byte, serial1):
    func_desc, send_text = command_mapping[received_byte]
    
    if received_byte == b'5':
        system_state['light'] = "关闭"
        serial1.send_with_frame(send_text)
        print(f"执行：{func_desc}，当前灯状态：{system_state['light']}")
    elif received_byte == b'2':
        system_state['light'] = "打开"
        serial1.send_with_frame(send_text)
        print(f"执行：{func_desc}，当前灯状态：{system_state['light']}")
    elif received_byte == b'1':
        system_state['door'] = "打开"
        serial1.send_with_frame(send_text)
        print(f"执行：{func_desc}，当前门状态：{system_state['door']}")
    elif received_byte == b'6':
        system_state['alarm'] = "报警中"
        serial1.send_with_frame(send_text)
        print(f"执行：{func_desc}，当前报警状态：{system_state['alarm']}")


def handle_navigation_command(received_byte, nav_node, serial1):
    func_desc, _ = command_mapping[received_byte]
    
    if system_state['navigation'] == "navigating":
        print("当前正在执行导航任务，请等待完成后再发送新指令")
        return
    
    if received_byte == b'3':
        nav_node.send_goal(water_x, water_y, water_yaw)
        print(f"开始{func_desc}导航...")
        
        if nav_node.wait_for_completion():
            system_state['water_delivery'] = "已送"
            print(f"{func_desc}到达：打开水阀→放水→关闭水阀")
            serial1.send_with_frame(f"{func_desc}已完成，请取水")
            time.sleep(2)
        else:
            print(f"{func_desc}导航失败")
            serial1.send_with_frame(f"{func_desc}导航失败，请重试")
            
    elif received_byte == b'4':
        nav_node.send_goal(medicine_x, medicine_y, medicine_yaw)
        print(f"开始{func_desc}导航...")
        
        if nav_node.wait_for_completion():
            system_state['medicine_delivery'] = "已送"
            print(f"{func_desc}到达：打开药箱→提示取药→关闭药箱")
            serial1.send_with_frame(f"{func_desc}已完成，请取药")
            time.sleep(2)
        else:
            print(f"{func_desc}导航失败")
            serial1.send_with_frame(f"{func_desc}导航失败，请重试")


# --------------------------
# 主程序
# --------------------------
def main():
    rclpy.init()
    nav_node = NavigationNode()
    
    serial1 = SerialCommunication(serial1_port, serial1_baudrate)
    serial2 = SerialCommunication(serial2_port, serial2_baudrate)
    
    if not serial1.open() or not serial2.open():
        print("串口打开失败，程序退出")
        return
    
    try:
        print("开始运行（按Ctrl+C退出）")
        print("等待串口2发送字节指令（如b'5'、b'3'等）...")
        while True:
            received_byte = serial2.receive_bytes()
            
            if received_byte:
                print(f"\n串口2收到：{received_byte} （十六进制：{received_byte.hex()}）")
                
                if received_byte in command_mapping:
                    if received_byte in [b'3', b'4']:
                        handle_navigation_command(received_byte, nav_node, serial1)
                    else:
                        handle_normal_command(received_byte, serial1)
                else:
                    print(f"未知指令：{received_byte}，忽略")
            
            rclpy.spin_once(nav_node, timeout_sec=0.1)
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\n用户终止程序")
    finally:
        serial1.close()
        serial2.close()
        nav_node.destroy_node()
        rclpy.shutdown()
        print("程序已退出")


if __name__ == "__main__":
    main()
import serial
import time
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from action_msgs.msg import GoalStatus

# --------------------------
# 基础配置
# --------------------------
# 串口配置
serial1_port = '/dev/ttyCH341USB0'
serial1_baudrate = 115200
serial2_port = '/dev/ttyCH341USB1'
serial2_baudrate = 9600

# 帧头帧尾
FRAME_HEADER = b'\x7B'
FRAME_FOOTER = b'\x7D'

# 指令映射
command_mapping = {
    b'5': ('关灯', '关闭所有灯光'),
    b'2': ('开灯', '打开所有灯光'),
    b'3': ('送水', ''),
    b'4': ('送药', ''),
    b'1': ('开门', '打开大门'),
    b'6': ('报警', '启动报警系统')
}

# 导航目标
water_x, water_y, water_yaw = 1.8, -0.5, -1.57
medicine_x, medicine_y, medicine_yaw = 1.8, 0.8, 1.57

# 状态变量
system_state = {
    'light': "关闭",
    'water_delivery': "未送",
    'medicine_delivery': "未送",
    'door': "关闭",
    'alarm': "未报警",
    'navigation': "idle"  # idle/navigating/completed/failed
}


# --------------------------
# ROS2导航节点（修复状态更新）
# --------------------------
class NavigationNode(Node):
    def __init__(self):
        super().__init__('navigation_controller')
        self.nav_publisher = self.create_publisher(PoseStamped, 'goal_pose', 10)
        self.status_sub = self.create_subscription(
            GoalStatus,
            '/goal_status',
            self.status_callback,
            10
        )
        self.current_goal_status = GoalStatus.STATUS_SUCCEEDED
        self.get_logger().info('ROS2导航节点已启动')

    def status_callback(self, msg):
        """增强状态更新日志，确保状态正确同步"""
        prev_status = self.current_goal_status
        self.current_goal_status = msg.status
        
        # 打印状态变化（方便调试）
        status_map = {
            GoalStatus.STATUS_SUCCEEDED: "成功",
            GoalStatus.STATUS_ACTIVE: "活跃",
            GoalStatus.STATUS_ABORTED: "失败",
            GoalStatus.STATUS_CANCELED: "取消"
        }
        self.get_logger().info(
            f"导航状态变化: {status_map.get(prev_status, '未知')} → {status_map.get(self.current_goal_status, '未知')}"
        )
        
        # 强制更新系统状态
        if self.current_goal_status == GoalStatus.STATUS_ACTIVE:
            system_state['navigation'] = "navigating"
        elif self.current_goal_status == GoalStatus.STATUS_SUCCEEDED:
            system_state['navigation'] = "completed"
        elif self.current_goal_status in [GoalStatus.STATUS_ABORTED, GoalStatus.STATUS_CANCELED]:
            system_state['navigation'] = "failed"

    def send_goal(self, x, y, yaw):
        goal_msg = PoseStamped()
        goal_msg.header.frame_id = 'map'
        goal_msg.header.stamp = self.get_clock().now().to_msg()
        goal_msg.pose.position.x = x
        goal_msg.pose.position.y = y
        goal_msg.pose.position.z = 0.0
        
        import math
        goal_msg.pose.orientation.z = math.sin(yaw / 2.0)
        goal_msg.pose.orientation.w = math.cos(yaw / 2.0)
        
        self.nav_publisher.publish(goal_msg)
        self.get_logger().info(f'已发送导航目标：x={x}, y={y}')
        system_state['navigation'] = "navigating"
        return True

    def wait_for_completion(self, timeout=30):
        """修复：确保导航完成后状态强制更新"""
        start_time = time.time()
        while rclpy.ok():
            # 每0.5秒打印一次当前状态（调试用）
            if int(time.time() - start_time) % 5 == 0:
                self.get_logger().info(f"等待导航完成...当前状态: {system_state['navigation']}")
            
            if system_state['navigation'] == "completed":
                # 强制重置状态为idle（关键修复）
                system_state['navigation'] = "idle"
                self.get_logger().info("导航完成，状态重置为空闲")
                return True
            if system_state['navigation'] == "failed":
                system_state['navigation'] = "idle"
                self.get_logger().info("导航失败，状态重置为空闲")
                return False
            if time.time() - start_time > timeout:
                self.get_logger().warn("导航超时，强制重置状态")
                system_state['navigation'] = "idle"  # 超时后强制重置
                return False
            
            rclpy.spin_once(self, timeout_sec=0.1)
            time.sleep(0.1)


# --------------------------
# 串口通信类（增加缓存清理）
# --------------------------
class SerialCommunication:
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.ser = None

    def open(self):
        try:
            if self.ser and self.ser.is_open:
                self.close()
            self.ser = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=1.0
            )
            if self.ser.is_open:
                print(f"串口 {self.port} 已打开")
                return True
            return False
        except Exception as e:
            print(f"打开串口 {self.port} 失败: {e}")
            return False

    def close(self):
        if self.ser and self.ser.is_open:
            self.ser.close()
            print(f"串口 {self.port} 已关闭")

    def send_with_frame(self, text):
        if not self.ser or not self.ser.is_open:
            print("串口未打开，无法发送")
            return False
        try:
            text_bytes = text.encode('utf-8')
            frame = FRAME_HEADER + text_bytes + FRAME_FOOTER
            self.ser.write(frame)
            print(f"串口1发送: {frame.hex()} （内容：{text}）")
            return True
        except Exception as e:
            print(f"串口1发送失败: {e}")
            return False

    def receive_bytes(self):
        """修复：读取后清空缓存，避免重复接收同一指令"""
        if not self.ser or not self.ser.is_open:
            return None
        try:
            data = self.ser.read(1)
            # 关键修复：如果有剩余数据，清空缓存（防止重复读取）
            if self.ser.in_waiting > 0:
                self.ser.read(self.ser.in_waiting)
            return data if data else None
        except Exception as e:
            print(f"串口2接收失败: {e}")
            return None


# --------------------------
# 命令处理函数
# --------------------------
def handle_normal_command(received_byte, serial1):
    func_desc, send_text = command_mapping[received_byte]
    
    if received_byte == b'5':
        system_state['light'] = "关闭"
        serial1.send_with_frame(send_text)
        print(f"执行：{func_desc}，当前灯状态：{system_state['light']}")
    elif received_byte == b'2':
        system_state['light'] = "打开"
        serial1.send_with_frame(send_text)
        print(f"执行：{func_desc}，当前灯状态：{system_state['light']}")
    elif received_byte == b'1':
        system_state['door'] = "打开"
        serial1.send_with_frame(send_text)
        print(f"执行：{func_desc}，当前门状态：{system_state['door']}")
    elif received_byte == b'6':
        system_state['alarm'] = "报警中"
        serial1.send_with_frame(send_text)
        print(f"执行：{func_desc}，当前报警状态：{system_state['alarm']}")


def handle_navigation_command(received_byte, nav_node, serial1):
    func_desc, _ = command_mapping[received_byte]
    
    if system_state['navigation'] == "navigating":
        print("当前正在执行导航任务，请等待完成后再发送新指令")
        return
    
    if received_byte == b'3':
        nav_node.send_goal(water_x, water_y, water_yaw)
        print(f"开始{func_desc}导航...")
        
        if nav_node.wait_for_completion():
            system_state['water_delivery'] = "已送"
            print(f"{func_desc}到达：打开水阀→放水→关闭水阀")
            serial1.send_with_frame(f"{func_desc}已完成，请取水")
            time.sleep(2)
        else:
            print(f"{func_desc}导航失败")
            serial1.send_with_frame(f"{func_desc}导航失败，请重试")
            
    elif received_byte == b'4':
        nav_node.send_goal(medicine_x, medicine_y, medicine_yaw)
        print(f"开始{func_desc}导航...")
        
        if nav_node.wait_for_completion():
            system_state['medicine_delivery'] = "已送"
            print(f"{func_desc}到达：打开药箱→提示取药→关闭药箱")
            serial1.send_with_frame(f"{func_desc}已完成，请取药")
            time.sleep(2)
        else:
            print(f"{func_desc}导航失败")
            serial1.send_with_frame(f"{func_desc}导航失败，请重试")


# --------------------------
# 主程序
# --------------------------
def main():
    rclpy.init()
    nav_node = NavigationNode()
    
    serial1 = SerialCommunication(serial1_port, serial1_baudrate)
    serial2 = SerialCommunication(serial2_port, serial2_baudrate)
    
    if not serial1.open() or not serial2.open():
        print("串口打开失败，程序退出")
        return
    
    try:
        print("开始运行（按Ctrl+C退出）")
        print("等待串口2发送字节指令（如b'5'、b'3'等）...")
        while True:
            received_byte = serial2.receive_bytes()
            
            if received_byte:
                print(f"\n串口2收到：{received_byte} （十六进制：{received_byte.hex()}）")
                
                if received_byte in command_mapping:
                    if received_byte in [b'3', b'4']:
                        handle_navigation_command(received_byte, nav_node, serial1)
                    else:
                        handle_normal_command(received_byte, serial1)
                else:
                    print(f"未知指令：{received_byte}，忽略")
            
            rclpy.spin_once(nav_node, timeout_sec=0.1)
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\n用户终止程序")
    finally:
        serial1.close()
        serial2.close()
        nav_node.destroy_node()
        rclpy.shutdown()
        print("程序已退出")


if __name__ == "__main__":
    main()
