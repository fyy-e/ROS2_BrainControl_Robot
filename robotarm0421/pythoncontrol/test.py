import time

import DrRobotController_Aloha_can as dr

'''''''''''''''''''''修改机器人参数函数'''''''''''''''''''''
# dr.write_param(id_num=1, property='dr.Aloha.config.l_1', value=152)
# dr.write_param(id_num=1, property='dr.Aloha.config.l_2', value=152)
# dr.write_param(id_num=1, property='dr.Aloha.config.l_3', value=70+1)
# dr.write_param(id_num=1, property='dr.Aloha.config.d_3', value=62+1)
# dr.write_param(id_num=1, property='dr.Aloha.config.l_p', value=0+1)
# dr.write_param(id_num=1, property='dr.Aloha.config.l_p_mass_center', value=0+1)
# dr.write_param(id_num=1, property='dr.Aloha.config.G_L_1', value=45+1)
# dr.write_param(id_num=1, property='dr.Aloha.config.G_L_2', value=30+1)
# dr.write_param(id_num=1, property='dr.Aloha.config.G_L_3', value=60+1)
# dr.write_param(id_num=1, property='dr.Aloha.config.G_L_4', value=106+1)
# dr.write_param(id_num=1, property='dr.Aloha.config.G_L_5', value=43+1)
# dr.write_param(id_num=1, property='dr.Aloha.config.G_L_6', value=62+1)
#
# dr.write_param(id_num=1, property='dr.Aloha.config.G_Gan_2', value=0.1005 + 0.001)
# dr.write_param(id_num=1, property='dr.Aloha.config.G_Gan_3', value=0.054 + 0.001)
# dr.write_param(id_num=1, property='dr.Aloha.config.G_Gan_4', value=0.057 + 0.001)
# dr.write_param(id_num=1, property='dr.Aloha.config.G_Gan_5', value=0.057 + 0.001)
# dr.write_param(id_num=1, property='dr.Aloha.config.G_3', value=0.329 + 0.001)
# dr.write_param(id_num=1, property='dr.Aloha.config.G_4', value=0.183 + 0.001)
# dr.write_param(id_num=1, property='dr.Aloha.config.G_5', value=0.253 + 0.001)
# dr.write_param(id_num=1, property='dr.Aloha.config.G_6', value=0.183 + 0.001)
# dr.write_param(id_num=1, property='dr.Aloha.config.G_p', value=0 + 0.001)
#
#
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_max_1', value=160 + 1)
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_max_2', value=180 + 1)
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_max_3', value=160 + 1)
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_max_4', value=160 + 1)
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_max_5', value=180 + 1)
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_max_6', value=180 + 1)
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_min_1', value=-160 + 1)
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_min_2', value=-40 + 1)
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_min_3', value=-160 + 1)
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_min_4', value=-160 + 1)
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_min_5', value=-180 + 1)
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_min_6', value=-180 + 1)
#
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_1', value=1 + 1)
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_2', value=1 + 1)
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_3', value=1 + 1)
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_4', value=1 + 1)
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_5', value=1 + 1)
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_6', value=1 + 1)
#
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_1', value=1 + 1)
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_2', value=1 + 1)
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_3', value=1 + 1)
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_4', value=1 + 1)
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_5', value=1 + 1)
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_6', value=1 + 1)

'''''''保存机器人参数函数'''''''
# dr.save_robot_config(id_num=1)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.l_1'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.l_2'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.l_3'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.d_3'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.l_p'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.l_p_mass_center'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_L_1'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_L_2'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_L_3'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_L_4'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_L_5'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_L_6'))
#
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_Gan_2'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_Gan_3'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_Gan_4'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_Gan_5'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_3'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_4'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_5'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_6'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_p'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_max_1'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_max_2'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_max_3'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_max_4'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_max_5'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_max_6'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_min_1'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_min_2'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_min_3'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_min_4'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_min_5'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_min_6'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_1'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_1'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_1'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_1'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_1'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_1'))
#
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_1'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_2'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_3'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_4'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_5'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_6'))
#
# print(dr.read_param(id_num=1, property='dr.robot.product_mode'))
# print(dr.read_param(id_num=1, property='dr.robot.can_id'))
# print(dr.read_param(id_num=1, property='dr.robot.pose_done'))
# print(dr.read_param(id_num=1, property='dr.robot.tip_can_id'))

'''''''实例化机器人函数'''''''
# dr.robot_instantiation(id_num=1)

'''''''运动到指定位置和姿态函数'''''''
# dr.set_pose(id_num=1, pl_temp=[200, 0, 100], theta_4_5_6=[0, 0, 0], speed=10, acceleration=10)

'''''''运动到指定位置函数'''''''
# dr.set_position(id_num=1, pl_temp=[200, 120, 230], speed=10, acceleration=10)
#
'''''''运动到指定姿态函数'''''''
# dr.set_4_5_6(id_num=1, theta_4_5_6=[0, 0, 0], speed=10, acceleration=10)

'''''''运动到相对位置和姿态函数'''''''
# dr.set_relative_pose(id_num=1, pl_temp=[0, 0, -10],  theta_4_5_6=[0, 0, 0], speed=10, acceleration=10)

'''''''运动到相对位置函数'''''''
# dr.set_relative_position(id_num=1, pl_temp=[10, 0, 0], speed=10, acceleration=10)

'''''''运动到相对姿态函数'''''''
# dr.set_relative_4_5_6(id_num=1, theta_4_5_6=[0, 0, 0], speed=10, acceleration=10)

'''''''等待运动到位函数'''''''
# speed = 50
# while 1:
#     dr.set_pose(id_num=1, pl_temp=[220, -0, 100], theta_4_5_6=[0, 0, 0], speed=speed, acceleration=speed)
#     dr.pose_done(id_num=1)
#     print(1)
#     dr.set_pose(id_num=1, pl_temp=[250, 152, 0], theta_4_5_6=[0, 0, 0], speed=speed, acceleration=speed)
#     dr.pose_done(id_num=1)
#     print(2)
#     dr.set_pose(id_num=1, pl_temp=[290, -152, 100], theta_4_5_6=[0, 90, 0], speed=speed, acceleration=speed)
#     dr.pose_done(id_num=1)
#     print(3)
#     dr.set_pose(id_num=1, pl_temp=[120, -0, 100], theta_4_5_6=[0, 0, 0], speed=speed, acceleration=speed)
#     dr.pose_done(id_num=1)
#     print(4)


'''''''机器人急停函数'''''''
# dr.set_pose(id_num=1, pl_temp=[220, -0, 100], theta_4_5_6=[0, 0, 0], speed=1, acceleration=1)
# time.sleep(1)
# dr.robot_estop(id_num=1)

'''''''查看当前末端坐标x_y_z函数（内存中）'''''''
# while 1:
#     print(dr.show_pose_x_y_z(id_num=1))

'''''''查看当前末端姿态4_5_6函数（内存中）'''''''
# while 1:
#     print(dr.show_pose_4_5_6(id_num=1))

'''''''查看当前模型关节角度函数（回读关节电机角度计算）'''''''
# while 1:
#     print(dr.detect_joints(id_num=1, n=6))

'''''''查看当前末端坐标x_y_z函数（回读关节电机角度计算）'''''''
# while 1:
#     print(dr.detect_pose_x_y_z(id_num=1))

'''''''查看当前末端姿态4_5_6函数（回读关节电机角度计算）'''''''
# while 1:
#     print(dr.detect_pose_4_5_6(id_num=1))

'''''''重力补偿'''''''
# start = time.time()
# t=0
# while(t<10):
#     dr.gravity_compensation(id_num=1, pay_load=0)
#     t = time.time() - start
# dr.out_of_gravity_compensation(id_num=1)

'''''''退出重力补偿'''''''
# start = time.time()
# t=0
# while(t<10):
#     dr.gravity_compensation(id_num=1, pay_load=0)
#     t = time.time() - start
# dr.out_of_gravity_compensation(id_num=1)

'''''''零力拖动'''''''
# dr.zero_force_pull(id_num=1, pay_load=0)

'''''''关节阻抗'''''''
# dr.impedance_control_joints(id_num=1, kp=0.1, kd=0.1)

'''''''轨迹示教（编程）'''''''
# dr.tutorial_program(id_num=1, pay_load=0, F=[0, 0, 0], n=500, t=10)

'''''''轨迹示教（执行）'''''''
# dr.tutorial_do(id_num=1, t=10)

'''''''待机'''''''
# dr.free(id_num=1)

'''''''位姿示教（编程）'''''''
# dr.add_pose(id_num=1, t=1)

'''''''锁住'''''''
# dr.lock(id_num=1)

'''''''位姿示教（执行）'''''''
# dr.do_pose(id_num=1, speed=10, acceleration=10, o_r=0, n=0)

'''''''''''''''''''''轨迹规划函数'''''''''''''''''''''
'''''''画正方形'''''''
def draw_rectangle(pl=[283, 0, -126.5], l=30, h=30):
    ''''在水平面上画正方形
    pl: 长方形左上角坐标（起始点），其中pl[2]代表作图平面与全局坐标系z轴的焦点的z坐标
    l: 宽度
    h: 高度
    '''
    n= 49 # 每条边分割的点数（数量越多画得越慢）
    l_delta = l/n
    h_delta = h/n
    pl_list = []
    pl_list.append(pl)
    l1 = pl[1]
    for i in range(1, n+1):
        pl_temp = [pl[0], pl[1]-i*l_delta, pl[2]]
        pl_list.append(pl_temp)
    # print(pl_temp)
    for i in range(1, n+1):
        pl_temp1 = [pl_temp[0]-i*h_delta, pl_temp[1], pl_temp[2]]
        pl_list.append(pl_temp1)
    # print(pl_temp1)
    for i in range(1, n+1):
        pl_temp2 = [pl_temp1[0], pl_temp1[1]+i*l_delta, pl_temp1[2]]
        pl_list.append(pl_temp2)
    # print(pl_temp2)
    for i in range(1, n+1):
        pl_temp3 = [pl_temp2[0]+i*h_delta, pl_temp2[1], pl_temp2[2]]
        pl_list.append(pl_temp3)
    # print(pl_temp3)
    # print(pl_list)
    return pl_list
#
#
pl_list = draw_rectangle(pl=[310, 50, 50], l=100, h=120) #
# print(pl_list)
#
# # ########控制机械臂末端连续运动到多个指定位置和姿态函数(必须单独一次性使用)
# # # ro.set_poses(pls_temp=pl_list, theta_P_R_Ys_temp=[[0, 90, 0]], t=10) # 控制机械臂末端连续运动到多个指定位置和姿态函数(必须单独一次性使用)
dr.set_poses_curve_pre(id_num=1, pls_temp=pl_list, theta_4_5_6s_temp=[[0, 0, 0]]) # 预设机械臂末端轨迹函数
time.sleep(1)
dr.set_poses_curve_do(id_num=1, t=10) # 末端轨迹执行函数，参数为大致运行时间

'''''''''''''''''''''读取机器人参数函数'''''''''''''''''''''
# print(dr.read_param(id_num=1, property='dr.Aloha.config.l_1'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.l_2'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.l_3'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.d_3'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.l_p'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.l_p_mass_center'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_L_1'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_L_2'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_L_3'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_L_4'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_L_5'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_L_6'))
#
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_Gan_2'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_Gan_3'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_Gan_4'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_Gan_5'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_3'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_4'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_5'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_6'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_p'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_max_1'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_max_2'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_max_3'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_max_4'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_max_5'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_max_6'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_min_1'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_min_2'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_min_3'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_min_4'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_min_5'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_min_6'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_1'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_1'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_1'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_1'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_1'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_1'))
#
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_1'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_2'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_3'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_4'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_5'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_6'))
#
# print(dr.read_param(id_num=1, property='dr.robot.product_mode'))
# print(dr.read_param(id_num=1, property='dr.robot.config.can_id'))
# print(dr.read_param(id_num=1, property='dr.robot.pose_done'))
# print(dr.read_param(id_num=1, property='dr.robot.config.tip_can_id'))

'''''''''''''''''''''读取机器人关节电机参数函数'''''''''''''''''''''
# print(dr.read_joint_motor_property(id_num=1, joint_num=1, property='dr.voltage'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=1, property='dr.i'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=1, property='dr.can.config.baud_rate'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=2, property='dr.can.config.enable_state_feedback'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=2, property='dr.version_date'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.config.can_id'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.config.state_feedback_rate_ms'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=5, property='dr.config.product_model'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.config.enable_angle_limit'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.config.angle_min'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.config.angle_max'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.config.gear_ratio'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.config.stall_current_limit'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.config.enable_crash_detect'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.config.crash_detect_sensitivity'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.config.enable_encoder_circular_limit'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.position_done'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.position_precision'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.config.enable_speed_limit'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.config.angle_gain'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.config.speed_gain'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.config.speed_integrator_gain'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.config.speed_limit'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.config.speed_limit_tolerance'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.config.inertia'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.config.input_filter_bandwidth'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.motor.config.torque_constant'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.motor.config.current_limit'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.motor.config.current_limit_margin'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.motor.config.torque_limit'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.motor.config.current_control_bandwidth'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.motor.Iq_measured'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.motor.Id_measured'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.board_temperature'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.board_temperature.config.enabled'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.board_temperature.config.temp_limit_lower'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.board_temperature.config.temp_limit_upper'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.motor_temperature'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.motor_temperature.config.enabled'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.motor_temperature.config.temp_limit_lower'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.motor_temperature.config.temp_limit_upper'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.output_shaft.angle'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.output_shaft.speed'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.output_shaft.torque'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.output_shaft.angle_min'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.output_shaft.angle_max'))
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.output_shaft.enable_angle_limit'))

'''''''''''''''''''''修改机器人参数函数'''''''''''''''''''''
# print(dr.read_param(id_num=1, property='dr.Aloha.config.l_1'))
# dr.write_param(id_num=1, property='dr.Aloha.config.l_1', value=1)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.l_1'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.l_2'))
# dr.write_param(id_num=1, property='dr.Aloha.config.l_2', value=2)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.l_2'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.l_3'))
# dr.write_param(id_num=1, property='dr.Aloha.config.l_3', value=3)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.l_3'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.d_3'))
# dr.write_param(id_num=1, property='dr.Aloha.config.d_3', value=4)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.d_3'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.l_p'))
# dr.write_param(id_num=1, property='dr.Aloha.config.l_p', value=5)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.l_p'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.l_p_mass_center'))
# dr.write_param(id_num=1, property='dr.Aloha.config.l_p_mass_center', value=6)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.l_p_mass_center'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_L_1'))
# dr.write_param(id_num=1, property='dr.Aloha.config.G_L_1', value=7)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_L_1'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_L_2'))
# dr.write_param(id_num=1, property='dr.Aloha.config.G_L_2', value=8)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_L_2'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_L_3'))
# dr.write_param(id_num=1, property='dr.Aloha.config.G_L_3', value=9)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_L_3'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_L_4'))
# dr.write_param(id_num=1, property='dr.Aloha.config.G_L_4', value=10)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_L_4'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_L_5'))
# dr.write_param(id_num=1, property='dr.Aloha.config.G_L_5', value=11)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_L_5'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_L_6'))
# dr.write_param(id_num=1, property='dr.Aloha.config.G_L_6', value=12)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_L_6'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_Gan_2'))
# dr.write_param(id_num=1, property='dr.Aloha.config.G_Gan_2', value=13)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_Gan_2'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_Gan_3'))
# dr.write_param(id_num=1, property='dr.Aloha.config.G_Gan_3', value=14)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_Gan_3'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_Gan_4'))
# dr.write_param(id_num=1, property='dr.Aloha.config.G_Gan_4', value=15)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_Gan_4'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_Gan_5'))
# dr.write_param(id_num=1, property='dr.Aloha.config.G_Gan_5', value=16)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_Gan_5'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_3'))
# dr.write_param(id_num=1, property='dr.Aloha.config.G_3', value=17)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_3'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_4'))
# dr.write_param(id_num=1, property='dr.Aloha.config.G_4', value=18)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_4'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_5'))
# dr.write_param(id_num=1, property='dr.Aloha.config.G_5', value=19)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_5'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_6'))
# dr.write_param(id_num=1, property='dr.Aloha.config.G_6', value=20)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_6'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_p'))
# dr.write_param(id_num=1, property='dr.Aloha.config.G_p', value=21)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.G_p'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_max_1'))
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_max_1', value=22)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_max_1'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_max_2'))
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_max_2', value=23)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_max_2'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_max_3'))
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_max_3', value=24)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_max_3'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_max_4'))
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_max_4', value=25)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_max_4'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_max_5'))
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_max_5', value=26)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_max_5'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_max_6'))
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_max_6', value=27)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_max_6'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_min_1'))
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_min_1', value=28)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_min_1'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_min_2'))
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_min_2', value=29)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_min_2'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_min_3'))
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_min_3', value=30)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_min_3'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_min_4'))
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_min_4', value=31)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_min_4'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_min_5'))
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_min_5', value=32)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_min_5'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_min_6'))
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_min_6', value=33)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_min_6'))
#
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_1'))
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_1', value=34)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_1'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_2'))
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_2', value=35)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_2'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_3'))
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_3', value=36)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_3'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_4'))
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_4', value=37)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_4'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_5'))
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_5', value=38)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_5'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_6'))
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_6', value=39)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_gear_ratio_6'))
#
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_1'))
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_1', value=40)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_1'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_2'))
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_2', value=41)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_2'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_3'))
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_3', value=42)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_3'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_4'))
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_4', value=43)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_4'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_5'))
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_5', value=44)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_5'))
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_6'))
# dr.write_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_6', value=45)
# print(dr.read_param(id_num=1, property='dr.Aloha.config.joints_torque_factor_6'))
#
# print(dr.read_param(id_num=1, property='dr.robot.can_id'))
# dr.write_param(id_num=1, property='dr.robot.can_id', value=46)
# print(dr.read_param(id_num=46, property='dr.robot.can_id'))
# dr.write_param(id_num=46, property='dr.robot.can_id', value=1) # id 号改回来
# print(dr.read_param(id_num=1, property='dr.robot.tip_can_id'))
# dr.write_param(id_num=1, property='dr.robot.tip_can_id', value=47)
# print(dr.read_param(id_num=1, property='dr.robot.tip_can_id'))


'''''''''''''''''''''修改机器人关节参数函数'''''''''''''''''''''
# print(dr.read_joint_motor_property(id_num=1, joint_num=1, property='dr.can.config.baud_rate'))
# dr.write_joint_motor_property(id_num=1, joint_num=1, property='dr.can.config.baud_rate', value=dr.read_joint_motor_property(id_num=1, joint_num=1, property='dr.can.config.baud_rate')+1)
# print(dr.read_joint_motor_property(id_num=1, joint_num=1, property='dr.can.config.baud_rate'))
#
# print(dr.read_joint_motor_property(id_num=1, joint_num=2, property='dr.can.config.enable_state_feedback'))
# dr.write_joint_motor_property(id_num=1, joint_num=2, property='dr.can.config.enable_state_feedback', value=1)
# print(dr.read_joint_motor_property(id_num=1, joint_num=2, property='dr.can.config.enable_state_feedback'))
#
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.config.state_feedback_rate_ms'))
# dr.write_joint_motor_property(id_num=1, joint_num=3, property='dr.config.state_feedback_rate_ms', value=1)
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.config.state_feedback_rate_ms'))
#
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.config.enable_angle_limit'))
# dr.write_joint_motor_property(id_num=1, joint_num=3, property='dr.config.enable_angle_limit', value=0)
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.config.enable_angle_limit'))
#
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.config.angle_min'))
# dr.write_joint_motor_property(id_num=1, joint_num=3, property='dr.config.angle_min', value=10)
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.config.angle_min'))
#
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.config.angle_max'))
# dr.write_joint_motor_property(id_num=1, joint_num=3, property='dr.config.angle_max', value=180)
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.config.angle_max'))
#
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.config.stall_current_limit'))
# dr.write_joint_motor_property(id_num=1, joint_num=3, property='dr.config.stall_current_limit', value=49.8)
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.config.stall_current_limit'))
#
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.config.enable_crash_detect'))
# dr.write_joint_motor_property(id_num=1, joint_num=3, property='dr.config.enable_crash_detect', value=0)
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.config.enable_crash_detect'))
#
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.config.crash_detect_sensitivity'))
# dr.write_joint_motor_property(id_num=1, joint_num=3, property='dr.config.crash_detect_sensitivity', value=149.8)
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.config.crash_detect_sensitivity'))
#
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.config.enable_encoder_circular_limit'))
# dr.write_joint_motor_property(id_num=1, joint_num=3, property='dr.config.enable_encoder_circular_limit', value=1)
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.config.enable_encoder_circular_limit'))
#
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.position_precision'))
# dr.write_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.position_precision', value=13.7)
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.position_precision'))
#
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.config.enable_speed_limit'))
# dr.write_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.config.enable_speed_limit', value=0)
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.config.enable_speed_limit'))
#
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.config.angle_gain'))
# dr.write_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.config.angle_gain', value=10.68)
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.config.angle_gain'))
#
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.config.speed_gain'))
# dr.write_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.config.speed_gain', value=0.42)
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.config.speed_gain'))
#
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.config.speed_integrator_gain'))
# dr.write_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.config.speed_integrator_gain', value=5.2)
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.config.speed_integrator_gain'))
#
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.config.speed_limit'))
# dr.write_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.config.speed_limit', value=10)
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.config.speed_limit'))
#
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.config.speed_limit_tolerance'))
# dr.write_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.config.speed_limit_tolerance', value=1.3)
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.config.speed_limit_tolerance'))
#
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.config.inertia'))
# dr.write_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.config.inertia', value=0.01)
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.config.inertia'))
#
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.config.input_filter_bandwidth'))
# dr.write_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.config.input_filter_bandwidth', value=21)
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.controller.config.input_filter_bandwidth'))
#
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.motor.config.current_limit'))
# dr.write_joint_motor_property(id_num=1, joint_num=3, property='dr.motor.config.current_limit', value=23.98)
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.motor.config.current_limit'))
#
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.motor.config.current_limit_margin'))
# dr.write_joint_motor_property(id_num=1, joint_num=3, property='dr.motor.config.current_limit_margin', value=1.2)
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.motor.config.current_limit_margin'))
#
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.motor.config.torque_limit'))
# dr.write_joint_motor_property(id_num=1, joint_num=3, property='dr.motor.config.torque_limit', value=90.1)
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.motor.config.torque_limit'))
#
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.motor.config.current_control_bandwidth'))
# dr.write_joint_motor_property(id_num=1, joint_num=3, property='dr.motor.config.current_control_bandwidth', value=21.2)
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.motor.config.current_control_bandwidth'))
#
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.board_temperature.config.enabled'))
# dr.write_joint_motor_property(id_num=1, joint_num=3, property='dr.board_temperature.config.enabled', value=0)
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.board_temperature.config.enabled'))
#
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.board_temperature.config.temp_limit_lower'))
# dr.write_joint_motor_property(id_num=1, joint_num=3, property='dr.board_temperature.config.temp_limit_lower', value=110)
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.board_temperature.config.temp_limit_lower'))
#
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.board_temperature.config.temp_limit_upper'))
# dr.write_joint_motor_property(id_num=1, joint_num=3, property='dr.board_temperature.config.temp_limit_upper', value=119)
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.board_temperature.config.temp_limit_upper'))
#
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.motor_temperature.config.enabled'))
# dr.write_joint_motor_property(id_num=1, joint_num=3, property='dr.motor_temperature.config.enabled', value=0)
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.motor_temperature.config.enabled'))
#
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.motor_temperature.config.temp_limit_lower'))
# dr.write_joint_motor_property(id_num=1, joint_num=3, property='dr.motor_temperature.config.temp_limit_lower', value=79)
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.motor_temperature.config.temp_limit_lower'))
#
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.motor_temperature.config.temp_limit_upper'))
# dr.write_joint_motor_property(id_num=1, joint_num=3, property='dr.motor_temperature.config.temp_limit_upper', value=99)
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.motor_temperature.config.temp_limit_upper'))
#
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.output_shaft.angle_min'))
# dr.write_joint_motor_property(id_num=1, joint_num=3, property='dr.output_shaft.angle_min', value=-178.2)
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.output_shaft.angle_min'))
#
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.output_shaft.angle_max'))
# dr.write_joint_motor_property(id_num=1, joint_num=3, property='dr.output_shaft.angle_max', value=178.2)
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.output_shaft.angle_max'))
#
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.output_shaft.enable_angle_limit'))
# dr.write_joint_motor_property(id_num=1, joint_num=3, property='dr.output_shaft.enable_angle_limit', value=1)
# print(dr.read_joint_motor_property(id_num=1, joint_num=3, property='dr.output_shaft.enable_angle_limit'))

'''''''''''''''''''''保存机器人关节参数函数'''''''''''''''''''''
# dr.motor_control_save_config(id_num=1, joint_num=5)

'''''''''''''''''''''单关节电机设置零点位置函数'''''''''''''''''''''
# dr.motor_control_set_zero_position(id_num=1, joint_num=5)

'''''''''''''''''''''单关节电机绝对角度控制函数'''''''''''''''''''''
# dr.motor_control_set_angle(id_num=1, joint_num=7, angle=10, speed=2, param=10, mode=1)

'''''''''''''''''''''单关节电机相对角度控制函数'''''''''''''''''''''
# dr.motor_control_step_angle(id_num=1, joint_num=2, angle=-10, speed=10, param=10, mode=1)

'''''''''''''''''''''单关节电机力位混合控制函数'''''''''''''''''''''
# dr.motor_control_set_angle_adaptive(id_num=1, joint_num=5, angle=-30, speed=1, torque=10)

'''''''''''''''''''''单关节电机阻抗控制函数'''''''''''''''''''''
# dr.motor_control_impedance_control(id_num=1, joint_num=5, angle=0, speed=1.2, tff=0.2, kp=1, kd=1)

'''''''''''''''''''''单关节电机运动助力函数'''''''''''''''''''''
# dr.motor_control_motion_aid(id_num=1, joint_num=5, angle=-90, speed=3.3, angle_err=0.1, speed_err=0.2, torque=10)

'''''''''''''''''''''单关节电机转速控制函数'''''''''''''''''''''
# dr.motor_control_set_speed(id_num=1, joint_num=5, speed=10, param=1, mode=1)

'''''''''''''''''''''等待单关节电机转动到位函数'''''''''''''''''''''
# dr.motor_control_set_angle(id_num=1, joint_num=5, angle=10, speed=10, param=10, mode=1)
# dr.motor_control_position_done(id_num=1, joint_num=5)
# dr.motor_control_set_angle(id_num=1, joint_num=5, angle=0, speed=10, param=10, mode=1)

'''''''''''''''''''''单关节电机转速控制函数 & 急停函数'''''''''''''''''''''
# dr.motor_control_set_speed(id_num=1, joint_num=5, speed=-10, param=10, mode=1)
# time.sleep(2)
# dr.motor_control_estop(id_num=1, joint_num=5)


'''''''''''''''''''''单关节电机力矩控制函数 & 急停函数'''''''''''''''''''''
# dr.motor_control_set_torque(id_num=1, joint_num=5, torque=10, param=5, mode=1)
# time.sleep(2)
# dr.motor_control_estop(id_num=1, joint_num=5)


'''''''''''''''''''''单关节电机转速自适应函数'''''''''''''''''''''
# dr.motor_control_set_speed(id_num=1, joint_num=5, speed=10, param=10, mode=1)
# time.sleep(1)
# dr.motor_control_set_speed_adaptive(id_num=1, joint_num=5, speed_adaptive=1)
# time.sleep(2)
# dr.motor_control_estop(id_num=1, joint_num=5)

'''''''''''''''''''''单关节电机力矩自适应函数'''''''''''''''''''''
# dr.motor_control_set_torque(id_num=1, joint_num=5, torque=-5, param=5, mode=1)
# time.sleep(1)
# dr.motor_control_set_torque_adaptive(id_num=1, joint_num=5, torque_adaptive=1)
# time.sleep(1)
# dr.motor_control_estop(id_num=1, joint_num=5)
'''''''''''''''''''''例程结束'''''''''''''''''''''
