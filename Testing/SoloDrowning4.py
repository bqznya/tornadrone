from robomaster import robot
import time

# Подключение к дрону
drone = robot.Drone()


# Взлет
def takeoff():
    print("Взлет")
    drone.takeoff()
    time.sleep(5)  # Подождать 5 секунд после взлета


# Посадка
def land():
    print("Посадка")
    drone.land()


# Передача видео
def stream_video():
    print("Передача видео начата")
    drone.start_video_stream(display=True)  # display=True для просмотра видеопотока в окне
    time.sleep(10)  # Передача видео в течение 10 секунд
    drone.stop_video_stream()
    print("Передача видео завершена")


# Основная программа
if __name__ == "__main__":
    try:
        # Подключение к дрону
        drone.initialize(conn_type="sta")

        # Взлет
        takeoff()

        # Передача видео
        stream_video()

        # Посадка
        land()

    except Exception as e:
        print("Произошла ошибка:", e)

    finally:
        # Завершение работы с дроном
        drone.close()