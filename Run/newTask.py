def write_to_file(file_name, data):
    with open(file_name, 'w+', encoding='utf-8') as file:
        file.write(data)
# шаблоны для NewTask:
# robot_group.up(20).wait_for_completed() # вверх 20
# robot_group.down(20).wait_for_completed() # вниз 20
a = input("1:Задание мне!")
b = input("2:Задание мне!")
write_to_file("task1.txt", a)
write_to_file("task2.txt", b)


def append_to_file(file_name,data):
    with open(file_name, 'a') as file:
        file.write(data)


t1 = """
code = ('''robot_group.rotate(90).wait_for_completed()
robot_group.forward(30).wait_for_completed()
file.seek(0)
file.truncate()
file.write(code)
''')
"""
t2 = """
code = ('''robot_group.rotate(-90).wait_for_completed()
robot_group.forward(30).wait_for_completed()
file.seek(0)
file.truncate()
file.write(code)
''')
"""
append_to_file("task1.txt",t1)
append_to_file("task2.txt",t2)