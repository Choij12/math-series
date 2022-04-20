from math_series.series import fibonacci, lucas, sum_series

def test_fibonacci_9():
    expected = 34
    actual = fibonacci(9)
    assert expected == actual

def test_fibonacci_15():
    expected = 610
    actual = fibonacci(15)
    assert expected == actual

def test_lucas_10():
    expected = 123
    actual = lucas(10)
    assert expected == actual

def test_sum_series_fibonacci():
    expected = 13
    actual = sum_series(7, 0, 1)
    assert expected == actual

def test_sum_series_lucas():
    expected = 123
    actual = sum_series(10, 2, 1)
    assert expected == actual