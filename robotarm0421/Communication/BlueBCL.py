import serial
import time
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped

# --------------------------
# 基础配置
# --------------------------
# 串口配置
serial1_port = '/dev/ttyCH341USB0'  # 串口1：发送带帧头帧尾的文本指令
serial1_baudrate = 115200
serial2_port = '/dev/ttyCH341USB1'  # 串口2：接收字节指令（如b'5'）
serial2_baudrate = 9600

# 帧头帧尾（固定）
FRAME_HEADER = b'\x7B'  # 帧头：0x7B
FRAME_FOOTER = b'\x7D'  # 帧尾：0x7D

# 串口2收到的字节 与 对应功能 的映射
# 键：串口2收到的字节（如b'5'）
# 值：(功能描述, 串口1需要发送的文本)
command_mapping = {
    b'5': ('关灯', '打开所有灯光'),
    b'2': ('开灯', '关闭所有灯光'),
    b'3': ('送水', ''),  # 送水不通过串口1发送，用ROS2导航
    b'4': ('送药', ''),  # 送药不通过串口1发送，用ROS2导航
    b'1': ('开门', '打开大门'),
    b'6': ('报警', '启动报警系统')
}

# 导航目标位置（送水/送药）
water_x, water_y, water_yaw = 2.5, 1.8, 1.57  # 送水坐标
medicine_x, medicine_y, medicine_yaw = 5.2, 3.3, 3.14  # 送药坐标

# 状态变量
light_state = "关闭"
water_state = "未送"
medicine_state = "未送"
door_state = "关闭"
alarm_state = "未报警"


# --------------------------
# ROS2导航节点
# --------------------------
class NavigationNode(Node):
    def __init__(self):
        super().__init__('navigation_controller')
        self.nav_publisher = self.create_publisher(PoseStamped, 'goal_pose', 10)
        self.get_logger().info('ROS2导航节点已启动')
        
    def send_goal(self, x, y, yaw):
        """发送导航目标（x,y坐标，yaw朝向）"""
        goal_msg = PoseStamped()
        goal_msg.header.frame_id = 'map'
        goal_msg.header.stamp = self.get_clock().now().to_msg()
        
        # 设置位置
        goal_msg.pose.position.x = x
        goal_msg.pose.position.y = y
        goal_msg.pose.position.z = 0.0
        
        # 转换朝向为四元数
        import math
        goal_msg.pose.orientation.z = math.sin(yaw / 2.0)
        goal_msg.pose.orientation.w = math.cos(yaw / 2.0)
        
        self.nav_publisher.publish(goal_msg)
        self.get_logger().info(f'导航目标：x={x}, y={y}')
        return True


# --------------------------
# 串口通信类
# --------------------------
class SerialCommunication:
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.ser = None

    def open(self):
        """打开串口"""
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
        """关闭串口"""
        if self.ser and self.ser.is_open:
            self.ser.close()
            print(f"串口 {self.port} 已关闭")

    def send_with_frame(self, text):
        """发送带帧头帧尾的文本（串口1专用）"""
        if not self.ser or not self.ser.is_open:
            print("串口未打开，无法发送")
            return False
        try:
            # 文本转字节，加上帧头帧尾
            text_bytes = text.encode('utf-8')
            frame = FRAME_HEADER + text_bytes + FRAME_FOOTER
            self.ser.write(frame)
            print(f"串口1发送: {frame.hex()} （内容：{text}）")
            return True
        except Exception as e:
            print(f"串口1发送失败: {e}")
            return False

    def receive_bytes(self):
        """接收字节指令（串口2专用，返回原始字节）"""
        if not self.ser or not self.ser.is_open:
            print("串口未打开，无法接收")
            return None
        try:
            # 读取数据（只需要判断收到的单个字节，如b'5'）
            data = self.ser.read(1)  # 读1个字节
            if data:
                return data  # 返回原始字节（如b'5'）
            return None
        except Exception as e:
            print(f"串口2接收失败: {e}")
            return None


# --------------------------
# 命令处理函数
# --------------------------
def handle_normal_command(received_byte, serial1):
    """处理普通命令（通过串口1发送文本）"""
    global light_state, door_state, alarm_state
    
    # 根据串口2收到的字节，从映射表中获取信息
    func_desc, send_text = command_mapping[received_byte]
    
    if received_byte == b'5':  # 收到b'5'→开灯
        light_state = "关闭"
        serial1.send_with_frame("关闭所有灯光")  # 发送"打开所有灯光"
        print(f"执行：{func_desc}，当前灯状态：{light_state}")
    elif received_byte == b'2':  # 收到b'2'→关灯
        light_state = "打开"
        serial1.send_with_frame("打开所有灯光")  # 发送"关闭所有灯光"
        print(f"执行：{func_desc}，当前灯状态：{light_state}")
    elif received_byte == b'1':  # 收到b'1'→开门
        door_state = "打开"
        serial1.send_with_frame(send_text)  # 发送"打开大门"
        print(f"执行：{func_desc}，当前门状态：{door_state}")
    elif received_byte == b'6':  # 收到b'6'→报警
        alarm_state = "报警中"
        serial1.send_with_frame(send_text)  # 发送"启动报警系统"
        print(f"执行：{func_desc}，当前报警状态：{alarm_state}")


def handle_navigation_command(received_byte, nav_node):
    """处理导航命令（送水/送药，调用ROS2）"""
    global water_state, medicine_state
    
    func_desc, _ = command_mapping[received_byte]
    
    if received_byte == b'3':  # 收到b'3'→送水
        # 1. 发送导航目标
        nav_node.send_goal(water_x, water_y, water_yaw)
        # 2. 模拟导航过程
        print(f"正在{func_desc}...")
        time.sleep(2)
        # 3. 执行送水操作
        water_state = "已送"
        print(f"{func_desc}到达：打开水阀→放水→关闭水阀")
        time.sleep(3)
        print(f"{func_desc}完成，当前状态：{water_state}")
    elif received_byte == b'4':  # 收到b'4'→送药
        # 1. 发送导航目标
        nav_node.send_goal(medicine_x, medicine_y, medicine_yaw)
        # 2. 模拟导航过程
        print(f"正在{func_desc}...")
        time.sleep(2)
        # 3. 执行送药操作
        medicine_state = "已送"
        print(f"{func_desc}到达：打开药箱→提示取药→关闭药箱")
        time.sleep(3)
        print(f"{func_desc}完成，当前状态：{medicine_state}")


# --------------------------
# 主程序
# --------------------------
def main():
    # 初始化ROS2
    rclpy.init()
    nav_node = NavigationNode()
    
    # 初始化串口
    serial1 = SerialCommunication(serial1_port, serial1_baudrate)  # 发送文本指令
    serial2 = SerialCommunication(serial2_port, serial2_baudrate)  # 接收字节指令
    
    # 打开串口
    if not serial1.open() or not serial2.open():
        print("串口打开失败，程序退出")
        return
    
    try:
        print("开始运行（按Ctrl+C退出）")
        print("等待串口2发送字节指令（如b'5'、b'3'等）...")
        while True:
            # 从串口2接收字节（如b'5'）
            received_byte = serial2.receive_bytes()
            
            if received_byte:
                print(f"\n串口2收到：{received_byte} （十六进制：{received_byte.hex()}）")
                
                # 检查收到的字节是否在我们的映射表中
                if received_byte in command_mapping:
                    # 区分普通命令和导航命令
                    if received_byte in [b'3', b'4']:  # 送水/送药
                        handle_navigation_command(received_byte, nav_node)
                    else:  # 其他命令（开灯/关灯等）
                        handle_normal_command(received_byte, serial1)
                else:
                    print(f"未知指令：{received_byte}，忽略")
            
            # 处理ROS2事件
            rclpy.spin_once(nav_node, timeout_sec=0.1)
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\n用户终止程序")
    finally:
        # 关闭资源
        serial1.close()
        serial2.close()
        nav_node.destroy_node()
        rclpy.shutdown()
        print("程序已退出")


if __name__ == "__main__":
    main()