class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start_engine(self):
        print(f"{self.brand} car started")
my_car = Car("Toyota", "Red")
my_car.start_engine()        



    