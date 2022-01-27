# PyTest
from unit_testing.simplecalc import SimpleCalc
import pytest

@pytest.fixture
def calc():
    return SimpleCalc()


def test_calc_add(calc):
    assert calc.add(6, 8) == 14


def test_calc_multiply(calc):
    assert pytest.approx(calc.multiply(0.4, -80.9)) == -32.36


def test_calc_divide(calc):
    assert calc.divide(10, 2) == 5.0


def test_calc_divide_by_zero_raises_error(calc):
    with pytest.raises(ZeroDivisionError):
        calc.divide(1, 0)