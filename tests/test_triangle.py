import pytest
from src.triangle import Triangle


@pytest.mark.parametrize(
    "a, b, c, expected_area, expected_perimeter",
    [
        (7, 10, 13, 34.64, 30)
    ]
)
def test_create_triangle_valid(a, b, c, expected_area, expected_perimeter):
    triangle = Triangle(a, b, c)
    assert triangle.area == expected_area, f"Expected area {expected_area}, got {triangle.area}"
    assert triangle.perimeter == expected_perimeter, \
        f"Expected perimeter {expected_perimeter}, got {triangle.perimeter}"


@pytest.mark.parametrize(
    ("a", "b", "c"),
    [
        (0, 0, 0),
        (-1, -2, 3),
        (5, 5, 12)
    ],
    ids=["zero value", "negative value", "invalid sides"]
)
def test_create_triangle_invalid(a, b, c):
    with pytest.raises(ValueError):
        Triangle(a, b, c)
