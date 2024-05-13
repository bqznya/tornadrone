from multi_robomaster import multi_robot
import time
from djitellopy import tello
import cv2

drone = tello.Tello()
drone.connect()
print(drone.get_battery())

while True:
    img = cv2.resize(drone.get_frame_read().frame,(360,240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)


def base_action_1(robot_group):
    with open('test1.txt', mode='r+',encoding='utf-8') as file:
        menu = True
        while menu:
            code = file.read()
            if (code!='Q'):
                exec(code)
                code = ("""robot_group.rotate(360).wait_for_completed()""")
                file.seek(0)
                file.truncate()
                file.write(code)
                file.close()
            else:
                robot_group.land().wait_for_completed()
                file.close()



def base_action_2(robot_group):
    with open('test2.txt', mode='r+',encoding='utf-8') as file:
        code = file.read()
        if (code!='Q'):
            exec(code)
            code = ('''robot_group.rotate(90).wait_for_completed()
                        robot_group.forward(30).wait_for_completed()
                        file.seek(0)
                        file.truncate()
                        file.write(code)
                        ''')
            file.seek(0)
            file.truncate()
            file.write(code)
        else:
            file.close()


if __name__ == '__main__':
    robot_sn_list = ['0TQZJAVCNT1BKU', '0TQZHB9CNT0BH7'] # №2, №1 // 61e833,EFC8FC
    multi_drone = multi_robot.MultiDrone()
    multi_drone.initialize(robot_num=2)
    multi_drone.number_id_by_sn([0, robot_sn_list[0]], [1, robot_sn_list[1]])
    multi_drone_group1 = multi_drone.build_group([0])
    multi_drone_group2 = multi_drone.build_group([1])
    multi_drone.run([multi_drone_group1, base_action_1],
                    [multi_drone_group2, base_action_2])
    multi_drone.close()