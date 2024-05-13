from multi_robomaster import multi_robot
import time



def base_action_1(robot_group):
    with open('task1.txt', mode='r+',encoding='utf-8') as file:
        while True:
            code = file.read()
            if (code!="Q"):
                exec(code)
                code = ("""robot_group.rotate(90).wait_for_completed()
                robot_group.forward(30).wait_for_completed()
                file.seek(0)
                file.truncate()
                file.write(code)""")
                file.seek(0)
                file.truncate()
                file.write(code)
            else:
                robot_group.land().wait_for_completed()
                file.close()



def base_action_2(robot_group):
    with open('task2.txt', mode='r+',encoding='utf-8') as file:
        while True:
            code = file.read()
            if (code!="Q"):
                exec(code)
                code = ('''robot_group.rotate(-90).wait_for_completed()
robot_group.forward(30).wait_for_completed()''')
                file.seek(0)
                file.truncate()
                file.write(code)
                file.close()
            else:
                robot_group.land().wait_for_completed()
                file.close()


if __name__ == '__main__':
    robot_sn_list = ['0TQZJAVCNT1BKU', '0TQZHB9CNT0BH7'] # №2, №1 // 61e833,EFC8FC
    multi_drone = multi_robot.MultiDrone()
    multi_drone.initialize(robot_num=2)
    multi_drone.number_id_by_sn([0, robot_sn_list[0]], [1, robot_sn_list[1]])
    drone_ip_list = multi_drone._get_sn(timeout=10)
    for sn in drone_ip_list:
        print("scan result: sn:{0}, ip:{1}".format(sn, drone_ip_list[sn]))
    multi_drone_group1 = multi_drone.build_group([0])
    multi_drone_group2 = multi_drone.build_group([1])
    multi_drone.run([multi_drone_group1, base_action_1],
                    [multi_drone_group2, base_action_2])
    multi_drone.close()