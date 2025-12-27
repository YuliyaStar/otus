import pytest
from src.square import Square


@pytest.mark.parametrize(
    "side, expected_area, expected_perimeter",
    [
        (5, 25, 20)
    ]
)
def test_create_square(side, expected_area, expected_perimeter):
    square = Square(side)
    assert square.area == expected_area, f"Expected area {expected_area}, got {square.area}"
    assert square.perimeter == expected_perimeter, f"Expected perimeter {expected_perimeter}, got {square.perimeter}"


@pytest.mark.parametrize(
    "side",
    [0, -2],
    ids=["zero value", "negative value"]
)
def test_square_area_and_perimeter(side):
    with pytest.raises(ValueError):
        Square(side)
