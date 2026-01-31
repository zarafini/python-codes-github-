class BMW:
    def fuel_type(self):
        print("BMW uses Petrol")

    def max_speed(self):
        print("BMW maximum speed is 250 km/h")

class Ferrari:
    def fuel_type(self):
        print("Ferrari uses Petrol")

    def max_speed(self):
        print("Ferrari maximum speed is 340 km/h")

def vehicleinfo(vehicle):
    vehicle.fuel_type()
    vehicle.max_speed()

bmw = BMW()
ferrari = Ferrari()

vehicleinfo(bmw)
print()
vehicleinfo(ferrari)