import pytest
from src.prueba1 import comparador

def test_comparador():
    assert comparador(1, 1) == 0
    assert comparador(3, 2) == 3
    assert comparador(2, 3) == 3

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        (1, 1, 0),
        (0, 0, 0),
        (100, -100, 100),
        (-15, -1, -1),
        (-3, 8, 8),
        (2, 0, 2)
    ]
)
def test_comparador_params(input_n1, input_n2, expected):
    assert comparador(input_n1, input_n2) == expected
    
    