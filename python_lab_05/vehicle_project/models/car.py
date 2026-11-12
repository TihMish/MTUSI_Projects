from models.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def get_info(self):
        return f"Автомобиль: {super().get_info()}, дверей: {self.doors}"

    def move(self):
        return f"Автомобиль {self.brand} едет по дороге"
