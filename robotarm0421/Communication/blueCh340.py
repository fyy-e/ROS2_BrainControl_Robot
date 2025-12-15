import serial
import time
from typing import Optional, Union

class SerialCommunication:
    def __init__(self, port: str = '/dev/ttyCH341USB0', baudrate: int = 115200, 
                 timeout: float = 1.0, parity: str = 'N', 
                 stopbits: float = 1, bytesize: int = 8,
                 header: bytes = b'\x7B',  # 包头：0x7B（十六进制）
                 footer: bytes = b'\x7D'): # 包尾：0x7D（十六进制）
        """
        初始化串口通信对象（自动添加包头包尾）
        
        :param port: 串口设备路径，如'/dev/ttyCH341USB0'
        :param baudrate: 波特率
        :param header: 包头（默认0x7B）
        :param footer: 包尾（默认0x7D）
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.parity = self._get_parity(parity)
        self.stopbits = self._get_stopbits(stopbits)
        self.bytesize = self._get_bytesize(bytesize)
        self.header = header  # 包头（固定为7B）
        self.footer = footer  # 包尾（固定为7D）
        self.ser = None

    def _get_parity(self, parity: str) -> int:
        """转换校验位参数为pyserial常量"""
        parity_map = {
            'N': serial.PARITY_NONE,
            'E': serial.PARITY_EVEN,
            'O': serial.PARITY_ODD
        }
        return parity_map.get(parity.upper(), serial.PARITY_NONE)

    def _get_stopbits(self, stopbits: float) -> float:
        """转换停止位参数为pyserial常量"""
        stopbits_map = {
            1: serial.STOPBITS_ONE,
            2: serial.STOPBITS_TWO,
            1.5: serial.STOPBITS_ONE_POINT_FIVE
        }
        return stopbits_map.get(stopbits, serial.STOPBITS_ONE)

    def _get_bytesize(self, bytesize: int) -> int:
        """转换数据位参数为pyserial常量"""
        bytesize_map = {
            5: serial.FIVEBITS,
            6: serial.SIXBITS,
            7: serial.SEVENBITS,
            8: serial.EIGHTBITS
        }
        return bytesize_map.get(bytesize, serial.EIGHTBITS)

    def open(self) -> bool:
        """打开串口连接（逻辑不变）"""
        try:
            if self.ser and self.ser.is_open:
                self.close()
                
            self.ser = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                parity=self.parity,
                stopbits=self.stopbits,
                bytesize=self.bytesize,
                timeout=self.timeout
            )
            
            if self.ser.is_open:
                print(f"串口 {self.port} 已打开，波特率: {self.baudrate}")
                return True
            return False
            
        except serial.SerialException as e:
            print(f"打开串口失败: {str(e)}")
            return False

    def close(self) -> None:
        """关闭串口连接（逻辑不变）"""
        if self.ser and self.ser.is_open:
            self.ser.close()
            print(f"串口 {self.port} 已关闭")

    def send_data(self, data: Union[str, bytes], encoding: str = 'utf-8') -> bool:
        """
        发送数据（自动添加包头0x7B和包尾0x7D）
        """
        if not self.ser or not self.ser.is_open:
            print("串口未打开，请先调用open()方法")
            return False
            
        try:
            # 转换数据为字节
            if isinstance(data, str):
                data_bytes = data.encode(encoding)
            else:
                data_bytes = data
                
            # 构建完整数据包：包头 + 数据 + 包尾
            packet = self.header + data_bytes + self.footer
            
            # 发送数据包
            self.ser.write(packet)
            self.ser.flush()
            print(f"发送数据包（含包头包尾）: {packet.hex()}")  # 打印十六进制便于调试
            print(f"实际发送内容: {data}")
            return True
            
        except serial.SerialException as e:
            print(f"发送数据失败: {str(e)}")
            return False
        except UnicodeEncodeError as e:
            print(f"数据编码失败: {str(e)}")
            return False

    def receive_data(self, max_bytes: int = 1024, decode: bool = True, 
                    encoding: str = 'utf-8', extract_payload: bool = True) -> Optional[Union[str, bytes]]:
        """
        接收数据（可选择提取包头包尾之间的有效数据）
        
        :param extract_payload: 是否提取包头包尾之间的有效数据（默认True）
        """
        if not self.ser or not self.ser.is_open:
            print("串口未打开，请先调用open()方法")
            return None
            
        try:
            data = self.ser.read(max_bytes)
            if not data:
                return None

            # 如果需要提取有效数据（去除包头包尾）
            if extract_payload:
                # 检查是否包含完整的包头和包尾
                if self.header in data and self.footer in data:
                    # 找到包头和包尾的位置
                    header_idx = data.find(self.header)
                    footer_idx = data.find(self.footer, header_idx + 1)
                    if header_idx != -1 and footer_idx != -1:
                        # 提取包头后、包尾前的有效数据
                        payload = data[header_idx + len(self.header) : footer_idx]
                        data = payload  # 替换为有效数据
                    else:
                        print("数据不完整（包头包尾位置异常）")
                else:
                    print("数据不包含完整的包头或包尾")

            # 解码并返回
            if decode:
                try:
                    decoded_data = data.decode(encoding).strip()
                    print(f"接收有效数据: {decoded_data}")
                    return decoded_data
                except UnicodeDecodeError:
                    print(f"接收二进制有效数据: {data.hex()}")
                    return data
            else:
                print(f"接收二进制有效数据: {data.hex()}")
                return data
                
        except serial.SerialException as e:
            print(f"接收数据失败: {str(e)}")
            return None

    def receive_line(self, encoding: str = 'utf-8', extract_payload: bool = True) -> Optional[Union[str, bytes]]:
        """
        接收一行数据（以换行符结束，支持提取有效数据）
        """
        if not self.ser or not self.ser.is_open:
            print("串口未打开，请先调用open()方法")
            return None
            
        try:
            data = self.ser.readline()
            if not data:
                return None

            # 提取有效数据（去除包头包尾）
            if extract_payload and self.header in data and self.footer in data:
                header_idx = data.find(self.header)
                footer_idx = data.find(self.footer, header_idx + 1)
                if header_idx != -1 and footer_idx != -1:
                    data = data[header_idx + len(self.header) : footer_idx]

            # 解码并返回
            try:
                decoded_data = data.decode(encoding).strip()
                print(f"接收行有效数据: {decoded_data}")
                return decoded_data
            except UnicodeDecodeError:
                print(f"接收行二进制有效数据: {data.hex()}")
                return data
                
        except serial.SerialException as e:
            print(f"接收行数据失败: {str(e)}")
            return None


# 使用示例
if __name__ == "__main__":
    serial_comm = SerialCommunication(
        port='/dev/ttyCH341USB0',  # 你的设备端口
        baudrate=115200,
        timeout=1
    )
    serial_commBCL = SerialCommunication(
        port='/dev/ttyCH341USB1',  # 你的设备端口
        baudrate=9600,
        timeout=1
    )
    
    try:
        if serial_comm.open():
            serial_commBCL.open()
            # 发送数据（自动添加包头0x7B和包尾0x7D）
            serial_comm.send_data("打开所有灯光")
            
            # 循环接收（自动提取有效数据）
            print("开始接收数据（按Ctrl+C退出）...")
            while True:
                serial_comm.send_data("关闭所有灯光")
                time.sleep(3)
                serial_comm.send_data("打开所有灯光")
                time.sleep(3)
                serial_comm.send_data("好的，已关闭")
                time.sleep(3)
                serial_comm.send_data("好的，打开了")
                time.sleep(3)
    except KeyboardInterrupt:
        print("\n用户中断程序")
    finally:
        serial_comm.close()