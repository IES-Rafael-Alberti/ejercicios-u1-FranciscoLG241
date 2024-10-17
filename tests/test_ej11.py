import pytest
from src.ej11_def2 import suma_entero

def test_comparador():
    assert suma_entero(2) == 3
    assert suma_entero(3) == 6
    assert suma_entero(5) == 15

@pytest.mark.parametrize(
    "input_n1, expected",
    [
        (2, 3),
        (3, 6),
        (5, 15),
        (7, 28),
        (9, 45),
        (8, 36)
    ]
)
def test_calculador_params(input_n1, expected):
    assert suma_entero(input_n1) == expected
    