def write_to_file(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(data)


t1 = """
robot_group.takeoff().wait_for_completed() # взлет
robot_group.curve(x1=100, y1=150, z1=50, x2=300, y2=0, z2=30, speed=40).wait_for_completed()
robot_group.curve(x1=-50, y1=0, z1=70, x2=-400, y2=0, z2=55, speed=40).wait_for_completed()
code = ('''robot_group.rotate(90).wait_for_completed()
robot_group.forward(30).wait_for_completed()
file.seek(0)
file.truncate()
file.write(code)
''') # запись рекурсивной задачи
file.seek(0)
file.truncate() # тут же по идее файл и стирается нахуй, следующие строчки не работают следовательно
file.write(code)
"""
print(t1)
t2 = """robot_group.takeoff().wait_for_completed() # взлет
code = ('''robot_group.rotate(-90).wait_for_completed()
robot_group.forward(30).wait_for_completed()
file.seek(0)
file.truncate()# тут же по идее файл и стирается нахуй, следующие строчки не работают следовательно
file.write(code)
''') # запись рекурсивной задачи
file.seek(0)
file.truncate()
file.write(code)
robot_group.land().wait_for_completed()
"""
l1 = """
code = print(123)
file.seek(0)
file.truncate()
file.write(code)
"""
write_to_file("task1.txt", t1)
write_to_file("task2.txt", t2)
write_to_file("test1.txt", "print('testA')")
write_to_file("test2.txt", "print('testB')")
