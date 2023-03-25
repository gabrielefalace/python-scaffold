import pytest
from hypothesis import given, settings, example, Verbosity
import hypothesis.strategies as st
from src import main


def get_add_test_data():
    return [(3, 5, 8), (-2, -2, -4), (-1, 5, 4), (3, -5, -2), (0, 5, 5)]


@pytest.mark.parametrize('num1, num2, expected', get_add_test_data())
def test_add(num1, num2, expected):
    assert main.add(num1, num2) == expected


@settings(verbosity=Verbosity.verbose, max_examples=500)
@example(1, 2)
@given(st.integers(), st.integers())
def test_add_property(num1, num2):
    assert main.add(num1, num2) == num1 + num2
