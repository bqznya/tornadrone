def write_to_file(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(data)


t1 = """
robot_group.takeoff().wait_for_completed() # взлет
robot_group.curve(x1=50, y1=50, z1=50, x2=100, y2=0, z2=50, speed=40).wait_for_completed()
robot_group.curve(x1=-50, y1=-50, z1=50, x2=-100, y2=0, z2=50, speed=40).wait_for_completed()
robot_group.curve(x1=-50, y1=50, z1=50, x2=-100, y2=0, z2=50, speed=40).wait_for_completed()
robot_group.curve(x1=50, y1=-50, z1=50, x2=100, y2=0, z2=50, speed=40).wait_for_completed()
code = ('''robot_group.rotate(90).wait_for_completed()
robot_group.forward(30).wait_for_completed()
''') # запись рекурсивной задачи
file.seek(0)
file.truncate()
file.write(code)
"""
t2 = """robot_group.takeoff().wait_for_completed() # взлет
code = ('''
robot_group.up(120).wait_for_completed()
robot_group.curve(x1=0, y1=50, z1=75, x2=0, y2=0, z2=100, speed=40).wait_for_completed()
robot_group.curve(x1=0, y1=-50, z1=-25, x2=0, y2=0, z2=-50, speed=40).wait_for_completed()
robot_group.curve(x1=0, y1=50, z1=-25, x2=0, y2=0, z2=-50, speed=40).wait_for_completed()
robot_group.curve(x1=0, y1=-50, z1=50, x2=0, y2=0, z2=100, speed=40).wait_for_completed()
''') # запись рекурсивной задачи
file.seek(0)
file.truncate()
file.write(code)
"""
l1 = """code = print(123)
file.seek(0)
file.truncate()
file.write(code)
"""
l2 = """code = print(321)
file.seek(0)
file.truncate()
file.write(code)
"""
write_to_file("task1.txt", t1)
write_to_file("task2.txt", t2)
write_to_file("test1.txt", l1)
write_to_file("test2.txt", l2)
