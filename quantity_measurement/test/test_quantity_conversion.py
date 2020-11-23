from quantity_measurement.main.quantities_measurement import *
import pytest


@pytest.mark.parametrize('first_type, first_value, second_type,second_value,result',
                         [(Lengths.feet, 1, Lengths.inch, 12, True), (Lengths.feet, 3, Lengths.yard, 1, True),
                          (Lengths.inch, 2, Lengths.cm, 5, True)])
def test_for_length_conversion(first_type, first_value, second_type, second_value, result):
    feet = QuantityMeasurer(first_type, first_value)
    inch = QuantityMeasurer(second_type, second_value)
    assert feet.compare(inch) == result

