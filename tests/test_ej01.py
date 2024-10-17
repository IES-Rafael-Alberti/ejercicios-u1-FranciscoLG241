import pytest
from src.ej01_def import solicitar_nombre_test

def test_nombre():
    assert solicitar_nombre_test("Fran") == "Fran"
    assert solicitar_nombre_test("Manolo") == "Manolo"
    assert solicitar_nombre_test("Messi") == "Messi"

@pytest.mark.parametrize(
    "input_n1, expected",
    [
        ("Fran", "Fran"),
        ("Manolo", "Manolo"),
        ("Sofía", "Sofía"),
        ("Alberto", "Alberto"),
        ("María", "María"),
        ("Alba", "Alba")
    ]
)
def test_comparador_params(input_n1, expected):
    assert solicitar_nombre_test(input_n1) == expected
    