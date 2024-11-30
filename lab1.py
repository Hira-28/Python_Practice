class Vehicle:
    def __init__(self, brand, model):
        self._brand = brand  # Protected attribute
        self.__model = model  # Protected attribute

    def display_info(self):
        print(f"Vehicle Brand: {self._brand}, Model: {self._model}")
v1=Vehicle("toyta",2024)
print(v1.__model)
class Car(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model)  # Call the parent class constructor
        self.year = year

    def display_car_info(self):
        # Accessing the protected variables from the parent class
        print(f"Car Brand: {self._brand}, Model: {self._model}, Year: {self.year}")

# Creating an instance of the subclass
my_car = Car("Toyota", "Corolla", 2020)

# Accessing protected attributes in subclass
my_car.display_car_info()  # Output: Car Brand: Toyota, Model: Corolla, Year: 2020
