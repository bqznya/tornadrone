from djitellopy import TelloSwarm


def drunk_logic(i, tello):
    if i % 2:
        with open('task1.txt', mode='r+', encoding='utf-8') as file:
            while True:
                code = file.read()
                if code != "Q":
                    exec(code)
                    code = ("""
                    tello.forward(30)
                    tello.rotate(90)
                    file.seek(0)
                    file.truncate()
                    file.write(code)""")
                    file.seek(0)
                    file.truncate()
                    file.write(code)
                else:
                    tello.land()
                    file.close()
        # tello.go_xyz_speed(-50, -50, 100, 50)
        # tello.curve_xyz_speed(100, 150, 50, 300, 0, 30, 40)
    else:
        with open('task2.txt', mode='r+', encoding='utf-8') as file:
            while True:
                code = file.read()
                if code != "Q":
                    exec(code)
                    code = ("""
                    tello.forward(30)
                    tello.rotate(-90)
                    file.seek(0)
                    file.truncate()
                    file.write(code)""")
                    file.seek(0)
                    file.truncate()
                    file.write(code)
                else:
                    tello.land()
                    file.close()


# tello.curve_xyz_speed(-50, 0, 70, -400, 0, 55, 40)


# swarm = TelloSwarm([test, west])
swarm = TelloSwarm.fromIps([
    "192.168.0.151",
    "192.168.0.185"
])
swarm.connect()
for tello in swarm:
    print(tello.get_battery())
swarm.takeoff()
swarm.parallel(drunk_logic)
# tl_flight.curve(x1=-50, y1=0, z1=70, x2=-400, y2=0, z2=55, speed=40).wait_for_completed() # y
swarm.end()
# swarm.send_rc_control(0, 50, 0, 0)
# sleep(2)
# swarm.land()
