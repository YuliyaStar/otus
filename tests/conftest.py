import pytest

'''
Fixtures for rectangle
'''
@pytest.fixture()
def get_rectangle_sides_area():

    def _wrapper(sides_type: str):
        if sides_type == 'integer':
            return 2, 4, 8

        if sides_type == 'float':
            return 2.1, 4.1, 8.61

        raise ValueError(f'Invalid sides type: float or integer')

    yield _wrapper


@pytest.fixture()
def get_rectangle_sides_perimeter():

    def _wrapper(sides_type: str):
        if sides_type == 'integer':
            return 2, 4, 12

        if sides_type == 'float':
            return 2.1, 4.1, 12.4

        raise ValueError(f'Invalid sides type: float or integer')

    yield _wrapper
