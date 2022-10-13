from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    started = False
    weight = 40
    fuel = float(500)
    fuel_consumption = 1

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def __repr__(self):
        return f"{self.__class__.__name__}(weight={self.weight}, fuel={self.fuel}, fuel_consumption={self.fuel_consumption})"

    def start(self):
        """engine starting"""
        if self.started is False:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("fuel is at zero")

    def move(self, path_length: float):
        """trip fuel check"""
        fuel_for_trip = path_length * self.fuel_consumption

        if self.fuel - fuel_for_trip < 0:
            raise NotEnoughFuel("not enough fuel for the trip")
        else:
            self.fuel -= fuel_for_trip



