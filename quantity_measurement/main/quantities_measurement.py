import enum
import logging
from quantity_measurement.main.measurement_exceptions import *

logging.basicConfig(filename="quantity.log", level=logging.DEBUG, format='%(asctime)s : %(levelname)s : %(message)s')


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
                logging.debug("Both the conversion values of {} and {} are equal".format(self.__unit, other.__unit))
                return True
            logging.debug("Both Quantity values are not equal")
            return False
        logging.debug("Both quantity types are not matching")
        raise TypeMismatchException("Both quantity types are not matching")

    def __add__(self, other):
        if self.__unit.__class__ == other.__unit.__class__:
            result = self.__unit.__class__.convert(self.__unit, self.__value) + other.__unit.__class__.convert(
                other.__unit, other.__value)
            logging.debug("addition of {} + {} is : {}".format(self.__value, other.__value, result))
            return result
        logging.debug("Both quantity types are not matching")
        raise TypeMismatchException("Both quantity types are not matching")


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
