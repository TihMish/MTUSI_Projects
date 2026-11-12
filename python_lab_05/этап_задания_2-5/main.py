from models.vehicle import Vehicle


def main():
    print("=== Задание 2: два объекта Vehicle ===")
    car1 = Vehicle("Toyota", "Camry", 2024)
    car2 = Vehicle("Lada", "Vesta", 2023)
    print(car1.brand, car1.model, car1.year, car1._speed)
    print(car2.brand, car2.model, car2.year, car2._speed)
    car1._speed = 60
    print("car1._speed =", car1._speed, "| car2._speed =", car2._speed)
    print("car1 is car2:", car1 is car2)

    print("\n=== Задание 3: методы ===")
    car = Vehicle("Toyota", "Camry", 2024)
    car.accelerate(50)
    print("accelerate(50):", car.speed)
    car.brake(20)
    print("brake(20):", car.speed)
    car.brake(100)
    print("brake(100):", car.speed)
    car.accelerate(40)
    car.stop()
    print("stop():", car.speed)
    print("get_info():", car.get_info())

    print("\n=== Задание 4: property ===")
    car.speed = 80
    print("car.speed = 80 ->", car.speed)
    try:
        car.speed = -10
    except ValueError as error:
        print("Ошибка:", error)

    print("\n=== Задание 5: __str__ ===")
    print(car)


if __name__ == "__main__":
    main()
