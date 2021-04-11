from chevy_volt import ChevyVolt
from ford_focus import FordFocus
from jeep_sahara import JeepSahara
from null_car import NullCar


def get_car(car_name):
    if car_name == "Chevy":
        return ChevyVolt()
    elif car_name == "Ford":
        return FordFocus()
    elif car_name == "Jeep":
        return JeepSahara()
    else:
        return NullCar(car_name)


for car_name in "Chevy", "Ford", "Jeep", "Tesla":
    car = get_car(car_name)
    car.start()
    car.stop()
