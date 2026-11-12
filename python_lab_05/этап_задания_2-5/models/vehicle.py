class Vehicle:
    category = "Транспорт"

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self._speed = 0

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if value < 0:
            raise ValueError("Скорость не может быть отрицательной")
        self._speed = value

    def accelerate(self, value):
        self.speed = self.speed + value

    def brake(self, value):
        new_speed = self.speed - value
        if new_speed < 0:
            new_speed = 0
        self.speed = new_speed

    def stop(self):
        self.speed = 0

    def get_info(self):
        return f"{self.brand} {self.model} ({self.year})"

    def __str__(self):
        return f"{self.brand} {self.model}, {self.year} г., скорость: {self.speed} км/ч"
