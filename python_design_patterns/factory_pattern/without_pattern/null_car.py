class NullCar:
    def __init__(self, car_name):
        self._car_name = car_name

    def start(self):
        print(F"Unknown car starting --> {self._car_name}")

    def stop(self):
        print(F"Unknown car stopping --> {self._car_name}")
