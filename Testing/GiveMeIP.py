from multi_robomaster import multi_robot


if __name__ == '__main__':


    # robomaster.config.LOCAL_IP_STR = "192.168.10.2"
    multi_drone = multi_robot.MultiDrone()
    # change the robot_num that you want to scan
    multi_drone.initialize(robot_num=2)
    drone_ip_list = multi_drone._get_sn(timeout=10)
    for sn in drone_ip_list:
        print("scan result: sn:{0}, ip:{1}".format(sn, drone_ip_list[sn]))