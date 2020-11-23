import enum


class QuantityMeasurer:
    def __init__(self, unit, value):
        self.__unit = unit
        self.__value = value

    def __eq__(self, other):
        if isinstance(other, QuantityMeasurer):
            return self.__value == other.__value

    def compare(self, other):
        if isinstance(self.__unit, Lengths) and isinstance(other.__unit, Lengths):
            return True
        return False


class Lengths(enum.Enum):
    feet = 12
    inch = 1.0
    yard = 36.0
    cm = 0.4

    def __init__(self, unit):
        self.unit = unit

    def convert(self, value):
        return self.unit * value
