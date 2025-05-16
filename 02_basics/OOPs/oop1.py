class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand # encapsulation
        self.model = model
        Car.total_car = Car.total_car + 1

    def full_details(self):
        return f"{self.__brand} : {self.model}"
    def getBrand(self): # getter
        return self.__brand

    def fuel_type(self):
        return "Petrol or Disel"
    @staticmethod
    def gen_desc():
        return "A mode of transport and are pretty cool!! "




class Elcetric_car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size  = battery_size
    def fuel_type(self):
        return "Electricity"


my_car = Car('BMW', "M4")
print(my_car.getBrand())
print(my_car.model)

my_new_car = Car("Suzuki", "Swift")
print(my_new_car.model)
print(my_new_car.full_details())
print(my_new_car.fuel_type())

my_electric_car = Elcetric_car("Tata", "Nexon EV", "45 kWh")
print(my_electric_car.battery_size)
print(my_electric_car.full_details())
print(my_electric_car.fuel_type())

print(Car.total_car) # 3


print(my_car.gen_desc())
print(Car.gen_desc())
