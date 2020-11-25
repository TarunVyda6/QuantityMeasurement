class MeasurementException(Exception):
    pass


class TypeMismatchException(MeasurementException):
    def __init__(self, message):
        self.message = message
