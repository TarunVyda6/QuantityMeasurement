from quantity_measurement.main.quantities_measurement import *
import pytest


@pytest.mark.parametrize('first_type, first_value, second_type,second_value,result',
                         [(Lengths.feet, 1, Lengths.inch, 12, True), (Lengths.feet, 3, Lengths.yard, 1, True),
                          (Lengths.inch, 2, Lengths.cm, 5, True), (Lengths.inch, 2, Lengths.cm, 6, False)])
def test_for_length_conversion(first_type, first_value, second_type, second_value, result):
    type_one = QuantityMeasurer(first_type, first_value)
    type_two = QuantityMeasurer(second_type, second_value)
    assert type_one.compare(type_two) == result


@pytest.mark.parametrize('first_type, first_value, second_type,second_value,result',
                         [(Lengths.feet, 1, Lengths.inch, 12, 24), (Lengths.inch, 12, Lengths.feet, 1, 24),
                          (Lengths.cm, 500, Lengths.meter, 5, 397)])
def test_for_adding_two_lengths(first_type, first_value, second_type, second_value, result):
    type_one = QuantityMeasurer(first_type, first_value)
    type_two = QuantityMeasurer(second_type, second_value)
    assert type_one.add(type_two) == result
