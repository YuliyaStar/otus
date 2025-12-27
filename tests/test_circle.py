import pytest
from src.circle import Circle


@pytest.mark.parametrize(
    "radius, expected_area, expected_perimeter",
    [(8, 201.06, 50.27)]
)
def test_create_circle(radius, expected_area, expected_perimeter):
    circle = Circle(radius)
    actual_area = circle.area
    actual_perimeter = circle.perimeter
    assert actual_area == expected_area, f"Expected area {expected_area}, got {actual_area}"
    assert actual_perimeter == expected_perimeter, f"Expected perimeter {expected_perimeter}, got {actual_perimeter}"


@pytest.mark.parametrize(
    "radius",
    [0, -5],
    ids=["zero value", "negative value"]
)
def test_circle_area_and_perimeter(radius):
    with pytest.raises(ValueError):
        Circle(radius)
