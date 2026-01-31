class Vehicle:
    def __init__(self, basefare):
        self.basefare = basefare

    def fare(self):
        return self.basefare


class Bus(Vehicle):
    def __init__(self, base_fare, charge):
        super().__init__(base_fare)
        self.charge= charge

    def totalfare(self):
        return self.base_fare + self.charge


fare= int(input("Enter base fare: "))
maintenance= int(input("Enter maintenance charge: "))

bus = Bus(fare, maintenance)
print("Total Bus Fare:", bus.totalfare())