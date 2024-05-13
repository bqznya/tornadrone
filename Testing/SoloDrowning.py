from robomaster import robot

# Подключение к дрону
tl_drone = robot.Drone()
tl_drone.initialize()
tl_flight = tl_drone.flight
# Взлет
tl_flight.takeoff().wait_for_completed()


# Начало передачи видео
tl_drone.camera.start_video_stream(display=True)

# Для примера, просто ждем 10 секунд, чтобы передать видео
# В реальном приложении, здесь могут быть другие действия
tl_drone.sleep(10)

# Остановка передачи видео
tl_drone.camera.stop_video_stream()

# Посадка
tl_flight.land().wait_for_completed()

# Отключение от дрона
tl_drone.close()