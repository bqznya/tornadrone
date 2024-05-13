
import cv2
from robomaster import robot

IP_

if __name__ == '__main__':

    tl_drone = robot.Drone()
    tl_drone.initialize()

    SN = tl_drone.get_sn()
    print("drone sn: {0}".format(SN))
    drone_version = tl_drone.get_sdk_version()
    print("Drone sdk version: {0}".format(drone_version))
    tl_camera = tl_drone.camera
    # 显示302帧图传
    tl_camera.start_video_stream(display=False)
    tl_camera.set_fps("high")
    tl_camera.set_resolution("high")
    tl_camera.set_bitrate(6)
    for i in range(0, 302):
        img = tl_camera.read_cv2_image()
        cv2.imshow("Drone", img)
        cv2.waitKey(1)
    tl_flight = tl_drone.flight

    # 起飞
    tl_flight.takeoff().wait_for_completed()

    # 曲线飞行
    tl_flight.curve(x1=60, y1=60, z1=0, x2=120, y2=0, z2=30, speed=30).wait_for_completed()
    tl_flight.curve(x1=-60, y1=60, z1=0, x2=-120, y2=0, z2=-30, speed=30).wait_for_completed()

    # 降落
    tl_flight.land().wait_for_completed()

    cv2.destroyAllWindows()
    tl_camera.stop_video_stream()

    tl_drone.close()