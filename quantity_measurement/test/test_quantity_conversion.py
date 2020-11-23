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


@pytest.mark.parametrize('first_type, first_value, second_type,second_value,result',
                         [(Weights.kilo_gram, 16, Weights.gram, 16000, True), (Weights.tonne, 0.026, Weights.gram,
                                                                               26000, True)])
def test_for_weight_conversion(first_type, first_value, second_type, second_value, result):
    type_one = QuantityMeasurer(first_type, first_value)
    type_two = QuantityMeasurer(second_type, second_value)
    assert type_one.compare(type_two) == result


@pytest.mark.parametrize('first_type, first_value, second_type,second_value,result',
                         [(Weights.kilo_gram, 16, Weights.gram, 16000, 32), (Weights.tonne, 15, Weights.kilo_gram,
                                                                             15000, 30000)])
def test_for_adding_two_weights(first_type, first_value, second_type, second_value, result):
    type_one = QuantityMeasurer(first_type, first_value)
    type_two = QuantityMeasurer(second_type, second_value)
    assert type_one.add(type_two) == result


@pytest.mark.parametrize('first_type, first_value, second_type,second_value,result',
                         [(Temperature.fahrenheit, 89.6, Temperature.celsius, 32, True)])
def test_for_temperature_conversion(first_type, first_value, second_type, second_value, result):
    type_one = QuantityMeasurer(first_type, first_value)
    type_two = QuantityMeasurer(second_type, second_value)
    assert type_one.compare(type_two) == result


@pytest.mark.parametrize('first_type, first_value, second_type,second_value,result',
                         [(Temperature.fahrenheit, 89.6, Temperature.celsius, 32, 179.2)])
def test_for_temperature_addition(first_type, first_value, second_type, second_value, result):
    type_one = QuantityMeasurer(first_type, first_value)
    type_two = QuantityMeasurer(second_type, second_value)
    assert type_one.add(type_two) == result
