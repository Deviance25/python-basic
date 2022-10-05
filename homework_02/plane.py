"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo: int
    max_cargo: int

    def __init__(self, weight, fuel, fuel_consumption, cargo, max_cargo):
        self.max_cargo = max_cargo
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.cargo = cargo

    def load_cargo(self, num):
        if self.cargo + num > self.max_cargo:
            raise CargoOverload("Too much cargo")
        else:
            self.cargo += num

    def remove_all_cargo(self):
        max_cargo = self.cargo
        self.cargo = 0
        return max_cargo

