import pytest
from src.ej02_def2 import operacion_horas

def test_comparador():
    assert operacion_horas(2, 2) == 4.0
    assert operacion_horas(3, 4) == 12.0
    assert operacion_horas(3, 1) == 3.0

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        (2, 1, 2.0),
        (3, 4, 12.0),
        (3, 1, 3.0),
        (3, 2, 6.0),
        (4, 5, 20.0),
        (8, 9, 72.0)
    ]
)
def test_calculador_params(input_n1, input_n2, expected):
    assert operacion_horas(input_n1, input_n2) == expected
    