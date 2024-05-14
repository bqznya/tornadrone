with open('test1.txt', mode='r+', encoding='utf-8') as file:
    while True:
        code = file.read()
        if code != "Q":
            exec(code)
        else:
            print("waiting for task")
