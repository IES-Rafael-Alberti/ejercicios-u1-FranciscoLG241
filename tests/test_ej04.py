import pytest
from src.ej04_def2 import grados_celsius

def test_grados():
    assert round(grados_celsius(66), 2) == 18.89
    assert round(grados_celsius(56), 2) == 13.33
    assert round(grados_celsius(98), 2) == 36.67

@pytest.mark.parametrize(
    "input_n1, expected",
    [
        (66, 18.89),
        (56, 13.33),
        (98, 36.67),
        (65, 18.33),
        (82, 27.78),
        (94, 34.44)
    ]
)
def test_grados_params(input_n1, expected):
    assert round(grados_celsius(input_n1), 2) == expected

    