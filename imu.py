import rclpy
from rclpy.node import Node
from mpu6050 import mpu6050
import geometry_msgs
import time

class MPU(Node):
    def __init__(self):
        super().__init__("mpu")
        self.sensor = mpu6050(0x68)
        self.get_logger().info('Streaming Mpu6050 data .........')
        self.timer = self.create_timer(0.1, self.readsensor)  # specify the frequency of reading sensor (here it is 0.1 second)

    def readsensor(self):
        self.accel_data = sensor.get_accel_data()
        # print(f'Accelerometer: {accel_data}')
        gyro_data = sensor.get_gyro_data()
        # print(f'Gyroscope: {gyro_data}')
        self.get_logger(f"Accel:{accel_data}, Gyro:{gyro_data}")
        

def main(args=None):
    rclpy.init(args=args)
    node = MPU()
    rclpy.spin(node)

if __name__=='__main__':
    main()  