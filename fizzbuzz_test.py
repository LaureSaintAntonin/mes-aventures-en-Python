from division import division


def test_should_make_division_with_three_and_return_zero():
    numerator = (1, 101)
    denominator = 3
    expected_value = 0

    assert division(numerator, denominator) == expected_value
