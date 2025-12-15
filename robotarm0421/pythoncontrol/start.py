import time
from time import sleep

import DrRobotController_Aloha_can as dr

def controlwave():
    i = 3
    dr.motor_control_set_angle(id_num=1, joint_num=2, angle=0, speed=10, param=20, mode=1)
    dr.motor_control_set_angle(id_num=1, joint_num=3, angle=-120, speed=10, param=20, mode=1)
    dr.motor_control_set_angle(id_num=1, joint_num=6, angle=90, speed=10, param=20, mode=1)
    sleep(3)
    # dr.tutorial_program(id_num=1, pay_load=0, F=[0, 0, 0], n=500, t=10)
    # dr.tutorial_do(id_num=1, t=10)
    # dr.set_pose(id_num=1, pl_temp=[200, 0, 100], theta_4_5_6=[0, 0, 0], speed=10, acceleration=10)
    while(i):
        dr.motor_control_set_angle(id_num=1, joint_num=5, angle=-30, speed=20, param=20, mode=1)
        sleep(1)
        dr.motor_control_set_angle(id_num=1, joint_num=5, angle=50, speed=20, param=20, mode=1)
        sleep(2)
        i-=1
    sleep(1)
    dr.motor_control_set_angle(id_num=1, joint_num=2, angle=45, speed=10, param=20, mode=1)
    dr.motor_control_set_angle(id_num=1, joint_num=3, angle=20, speed=10, param=20, mode=1)
    dr.motor_control_set_angle(id_num=1, joint_num=4, angle=0, speed=10, param=20, mode=1)
    dr.motor_control_set_angle(id_num=1, joint_num=5, angle=0, speed=10, param=20, mode=1)
    dr.motor_control_set_angle(id_num=1, joint_num=6, angle=90, speed=10, param=20, mode=1)
    dr.motor_control_set_angle(id_num=1, joint_num=7, angle=0, speed=10, param=20, mode=1)
    dr.motor_control_set_angle(id_num=1, joint_num=6, angle=90, speed=10, param=10, mode=1)

def controlGrab():
    dr.motor_control_set_angle(id_num=1, joint_num=1, angle=-90, speed=10, param=20, mode=1)
    sleep(3)
    dr.motor_control_set_angle(id_num=1, joint_num=2, angle=60, speed=10, param=20, mode=1)
    dr.motor_control_set_angle(id_num=1, joint_num=3, angle=25, speed=10, param=20, mode=1)
    dr.motor_control_set_angle(id_num=1, joint_num=4, angle=0, speed=10, param=20, mode=1)
    dr.motor_control_set_angle(id_num=1, joint_num=5, angle=120, speed=10, param=20, mode=1)
    dr.motor_control_set_angle(id_num=1, joint_num=6, angle=-60, speed=10, param=20, mode=1)
    dr.motor_control_set_angle(id_num=1, joint_num=7, angle=30, speed=10, param=20, mode=1)
    sleep(2)
    dr.motor_control_set_angle(id_num=1, joint_num=4, angle=56, speed=10, param=20, mode=1)
    # sleep(1)
    # dr.motor_control_set_angle(id_num=1, joint_num=7, angle=30, speed=10, param=20, mode=1)
    sleep(3)
    dr.motor_control_set_angle(id_num=1, joint_num=7, angle=0, speed=10, param=20, mode=1)
    sleep(1)
    dr.motor_control_set_angle(id_num=1, joint_num=4, angle=0, speed=10, param=20, mode=1)
    sleep(1)
    
    # dr.motor_control_set_angle(id_num=1, joint_num=2, angle=45, speed=10, param=20, mode=1)
    # dr.motor_control_set_angle(id_num=1, joint_num=3, angle=20, speed=10, param=20, mode=1)
    # dr.motor_control_set_angle(id_num=1, joint_num=4, angle=0, speed=10, param=20, mode=1)
    # dr.motor_control_set_angle(id_num=1, joint_num=5, angle=0, speed=10, param=20, mode=1)
    # dr.motor_control_set_angle(id_num=1, joint_num=6, angle=-90, speed=10, param=20, mode=1)
    # dr.motor_control_set_angle(id_num=1, joint_num=7, angle=0, speed=10, param=20, mode=1)
    # dr.motor_control_set_angle(id_num=1, joint_num=6, angle=90, speed=10, param=10, mode=1)
    # sleep(2)
    # dr.motor_control_set_angle(id_num=1, joint_num=1, angle=0, speed=10, param=10, mode=1)
    
    # dr.motor_control_set_angle(id_num=1, joint_num=7, angle=30, speed=10, param=20, mode=1)
    # sleep(3)
    # dr.motor_control_set_angle(id_num=1, joint_num=5, angle=120, speed=10, param=20, mode=1)
    # dr.motor_control_set_angle(id_num=1, joint_num=6, angle=-60, speed=10, param=20, mode=1)
    # dr.motor_control_set_angle(id_num=1, joint_num=7, angle=30, speed=10, param=20, mode=1)

def ArmReset():
    dr.motor_control_set_angle(id_num=1, joint_num=2, angle=45, speed=10, param=20, mode=1)
    dr.motor_control_set_angle(id_num=1, joint_num=3, angle=20, speed=10, param=20, mode=1)
    dr.motor_control_set_angle(id_num=1, joint_num=4, angle=0, speed=10, param=20, mode=1)
    dr.motor_control_set_angle(id_num=1, joint_num=5, angle=0, speed=10, param=20, mode=1)
    dr.motor_control_set_angle(id_num=1, joint_num=6, angle=-90, speed=10, param=20, mode=1)
    dr.motor_control_set_angle(id_num=1, joint_num=7, angle=0, speed=10, param=20, mode=1)
    dr.motor_control_set_angle(id_num=1, joint_num=6, angle=90, speed=10, param=10, mode=1)
    sleep(2)
    dr.motor_control_set_angle(id_num=1, joint_num=1, angle=0, speed=10, param=10, mode=1)
    sleep(4)

def main():
    # controlwave()
    controlGrab()
    # ArmReset()
    # control()
    # while 1:
    #     print(dr.detect_pose_x_y_z(id_num=1))
    # while 1:
    #     print(dr.show_pose_x_y_z(id_num=1))

if __name__ == '__main__':
    main()