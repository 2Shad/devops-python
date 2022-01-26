from car_class import Car, variable


new_car = Car(20, 220)
new_car.accelerate(100)
print(new_car.get_speed())


print(__name__)