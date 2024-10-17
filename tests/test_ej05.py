import pytest
from src.ej05_def2 import calcular_precio_final

def test_comparador():
    assert calcular_precio_final(2, 1) == 2.02
    assert calcular_precio_final(3, 4) == 3.12
    assert calcular_precio_final(3, 1) == 3.03

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        (2, 1, 2.02),
        (3, 4, 3.12),
        (3, 1, 3.03),
        (1, 2, 1.02),
        (4, 5, 4.20),
        (8, 9, 8.72)
    ]
)
def test_calculador_params(input_n1, input_n2, expected):
    assert calcular_precio_final(input_n1, input_n2) == expected
    