class Garage:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle):
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)
            return True
        return False

    def show_all(self):
        if not self.vehicles:
            print("Гараж пуст")
            return
        for number, vehicle in enumerate(self.vehicles, start=1):
            print(f"{number}. {vehicle.get_info()}")

    def find_by_brand(self, brand):
        found = []
        for vehicle in self.vehicles:
            if vehicle.brand.lower() == brand.lower():
                found.append(vehicle)
        return found
