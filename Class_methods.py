class Vehicle:
    def __init__(self, brand, doors, wheels=4):  # init function is used to make construction
        self.brand = brand
        self.doors = doors
        self.wheels = wheels

    def car_details(self, local_details):
        print(f"Hi, {local_details} I am your new car -->{self.brand}.\nI have {self.doors} doors.\nI have {self.wheels} wheels.\n")


vehicle = Vehicle("BMW", 2)
vehicle.car_details('US')

vehicle1 = Vehicle("SUV", 4, 3)
vehicle1.car_details("India")
