
import time
import robomaster
from robomaster import robot
from robomaster import flight


if __name__ == '__main__':
    tl_drone = robot.Drone()
    tl_drone.initialize()
    tl_flight = tl_drone.flight

    # 打开挑战卡检测
    # tl_flight.mission_pad_on()

    # 起飞
    tl_flight.takeoff().wait_for_completed()

    # 飞行到挑战卡上方
    # tl_flight.go(x=30, y=30, z=50, speed=30).wait_for_completed()
    # tl_flight.curve(x1=150, y1=150, z1=50, x2=300, y2=0, z2=50, speed=30).wait_for_completed() # z
    # tl_flight.curve(x1=-50, y1=150, z1=30, x2=-400, y2=150, z2=65, speed=30).wait_for_completed() # y
    # tl_flight.curve(x1=-50, y1=40, z1=-50, x2=-50, y2=-30, z2=30, speed=30).wait_for_completed()# x
    # АААААААААААААААААААААААА
    tl_flight.curve(x1=100, y1=150, z1=50, x2=300, y2=0, z2=30, speed=40).wait_for_completed() # z
    tl_flight.curve(x1=-50, y1=0, z1=70, x2=-400, y2=0, z2=55, speed=40).wait_for_completed() # y
    tl_flight.curve(x1=-200, y1=300, z1=120, x2=0, y2=400, z2=80, speed=40).wait_for_completed() # x
    # 降落
    # tl_flight.curve(x1=50, y1=50, z1=100, x2=100, y2=0, z2=100, speed=30, mid="m").wait_for_completed()
    tl_flight.land().wait_for_completed()

    # 关闭挑战卡检测

    tl_drone.close()