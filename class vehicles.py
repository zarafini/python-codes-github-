# 1. Create an __init__ method with arguments - max_speed and mileage
# 2. Create an object of class Vehicle and pass the maximum speed and mileage of the car
# 3. Print the values of max_speed and mileage by using the object

class Vehicle:
    def __init__ (self, maximum_speed, mileage):
        self.maximum_speed= maximum_speed
        self.mileage= mileage

ob= Vehicle(120, 20)
print(ob.maximum_speed)
print(ob.mileage)