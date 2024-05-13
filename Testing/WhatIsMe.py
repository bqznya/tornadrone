import robomaster
import cv2
from robomaster import robot


if __name__ == '__main__':
    robomaster.config.LOCAL_IP_STR = "192.168.10.2"
    tl_drone = robot.Drone()
    tl_drone.initialize()

    version = tl_drone.get_sdk_version()
    print("Drone Version: {0}".format(version))
    version = tl_drone.get_sdk_version()
    print("Drone SDK Version: {0}".format(version))
    SN = tl_drone.get_sn()
    print("drone sn: {0}".format(SN))
    tl_flight = tl_drone.flight
    tl_camera = tl_drone.camera
    tl_camera.start_video_stream(display=True)
    tl_flight.takeoff().wait_for_completed()
    tl_flight.go(x=100, y=100, z=30, speed=30).wait_for_completed()
    tl_flight.go(x=-100, y=-100, z=-30, speed=30).wait_for_completed()
    cv2.destroyAllWindows()
    tl_flight.land().wait_for_completed()
    tl_drone.close()