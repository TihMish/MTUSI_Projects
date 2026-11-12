from models.vehicle import Vehicle


class Bus(Vehicle):
    def __init__(self, brand, model, year, seats, route_number):
        super().__init__(brand, model, year)
        self.seats = seats
        self.route_number = route_number

    def get_info(self):
        return f"Автобус: {super().get_info()}, мест: {self.seats}, маршрут №{self.route_number}"

    def move(self):
        return f"Автобус {self.brand} едет по маршруту №{self.route_number}"
