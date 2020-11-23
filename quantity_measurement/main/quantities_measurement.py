import enum


class QuantityMeasurer:
    def __init__(self, unit, value):
        self.__unit = unit
        self.__value = value

    def __eq__(self, other):
        if isinstance(other, QuantityMeasurer):
            return self.__value == other.__value
        return False

    def compare(self, other):
        if self.__unit.__class__ == other.__unit.__class__:
            if self.__unit.__class__.convert(self.__unit, self.__value) == other.__unit.__class__.convert(other.__unit,
                                                                                                          other.__value):
                return True
        return False

    def add(self, other):
        if self.__unit.__class__ == other.__unit.__class__:
            return self.__unit.__class__.convert(self.__unit, self.__value) + other.__unit.__class__.convert(
                other.__unit, other.__value)
        return 0


class Lengths(enum.Enum):
    feet = 12
    inch = 1.0
    yard = 36.0
    cm = 0.4
    meter = 39.4

    def __init__(self, unit):
        self.unit = unit

    def convert(self, value):
        return self.unit * value


class Weights(enum.Enum):
    kilo_gram = 1.0
    gram = 0.001
    tonne = 1000

    def __init__(self, unit):
        self.unit = unit

    def convert(self, value):
        return self.unit * value


class Temperature(enum.Enum):
    celsius = 1.8
    fahrenheit = 1

    def __init__(self, unit):
        self.unit = unit

    def convert(self, value):
        if self == Temperature.celsius:
            return self.unit * value + 32
        else:
            return self.unit * value
