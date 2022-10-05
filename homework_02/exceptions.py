"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    """ Not enough fuel to start the engine """
    pass


class NotEnoughFuel(Exception):
    """ Not enough fuel for the trip """
    pass


class CargoOverload(Exception):
    """ Too much cargo """
    pass
