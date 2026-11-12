from models.vehicle import Vehicle


class Truck(Vehicle):
    def __init__(self, brand, model, year, max_load):
        super().__init__(brand, model, year)
        self.max_load = max_load

    def get_info(self):
        return f"Грузовик: {super().get_info()}, грузоподъёмность: {self.max_load} т"

    def move(self):
        return f"Грузовик {self.brand} везёт груз по трассе"
