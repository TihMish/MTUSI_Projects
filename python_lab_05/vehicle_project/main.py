from garage import Garage
from models import Vehicle, Car, Truck, Motorcycle, Bus


def demo_methods():
    print("=== Задания 3–5: методы, property, __str__ ===")
    car = Car("Toyota", "Camry", 2024, 4)
    car.accelerate(50)
    print("После accelerate(50):", car.speed)
    car.brake(20)
    print("После brake(20):", car.speed)
    car.brake(100)
    print("После brake(100):", car.speed)
    car.accelerate(30)
    car.stop()
    print("После stop():", car.speed)
    car.speed = 80
    print("После car.speed = 80:", car.speed)
    try:
        car.speed = -10
    except ValueError as error:
        print("Ошибка:", error)
    print(car)


def demo_inheritance():
    print("\n=== Задания 6–7: наследование ===")
    car = Car("Lada", "Vesta", 2023, 4)
    truck = Truck("КАМАЗ", "54901", 2022, 20)
    moto = Motorcycle("Урал", "Gear-Up", 2021, True)
    car.accelerate(60)
    print(car)
    print(car.get_info())
    print(truck.get_info())
    print(moto.get_info())


def demo_abstract():
    print("\n=== Задание 8: абстрактный класс ===")
    try:
        Vehicle("Test", "Test", 2020)
    except TypeError as error:
        print("Ошибка:", error)


def demo_polymorphism():
    print("\n=== Задания 9 и 12: полиморфизм ===")
    vehicles = [
        Car("Toyota", "Camry", 2024, 4),
        Truck("КАМАЗ", "54901", 2022, 20),
        Motorcycle("Урал", "Gear-Up", 2021, True),
        Bus("ЛиАЗ", "5292", 2020, 110, 37),
    ]
    for vehicle in vehicles:
        print(vehicle.move())
        print(vehicle.get_info())
    return vehicles


def demo_garage(vehicles):
    print("\n=== Задания 10 и 12: гараж ===")
    garage = Garage()
    for vehicle in vehicles:
        garage.add_vehicle(vehicle)
    garage.add_vehicle(Car("Toyota", "RAV4", 2025, 5))
    garage.show_all()

    print("\nПоиск по марке Toyota:")
    for vehicle in garage.find_by_brand("Toyota"):
        print(vehicle)

    print("\nУдаляем мотоцикл:")
    garage.remove_vehicle(vehicles[2])
    garage.show_all()


def main():
    demo_methods()
    demo_inheritance()
    demo_abstract()
    vehicles = demo_polymorphism()
    demo_garage(vehicles)


if __name__ == "__main__":
    main()
