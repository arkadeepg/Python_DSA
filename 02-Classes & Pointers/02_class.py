class Car:

    # Constructor
    def __init__(self, brand: str, fuel_type: str) -> None:
        self.brand = brand
        self.fuel_type = fuel_type

    # Destructor, not required as Python has an automated Garbage Collector
    def __del__(self) -> None:
        pass

    # Method
    def drive(self, distance: float) -> None:
        print(f"Driving {self.brand} for {distance}km [{self.fuel_type}]")

car1: Car = Car(brand="Volvo", fuel_type="Diesel")
car2: Car = Car(brand="BMW", fuel_type="Electric")

print(car1.brand)
print(car1.fuel_type)
car1.drive(distance=10)

# Delete object
del car1

print("\n")

print(car2.brand)
print(car2.fuel_type)
car2.drive(distance=10)
