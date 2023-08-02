from app.models.rover import Rover
import pytest

def test_turn_left():
    rover = Rover(0, 0, 'N')
    rover.turn_left()
    assert rover.coordinate == 'W'

def test_turn_right():
    rover = Rover(0, 0, 'N')
    rover.turn_right()
    assert rover.coordinate == 'E'

@pytest.mark.parametrize("initial_x, initial_y, initial_direction, expected_x, expected_y", [
    (0, 0, 'N', 0, 1),
    (0, 0, 'E', 1, 0),
    (1, 1, 'S', 1, 0),
    (1, 1, 'W', 0, 1),
])
def test_move(initial_x, initial_y, initial_direction, expected_x, expected_y):
    rover = Rover(initial_x, initial_y, initial_direction)
    rover.move()
    assert rover.x == expected_x
    assert rover.y == expected_y

def test_is_valid_coordinate():
    rover = Rover(0, 0, 'N')
    assert rover.is_valid_coordinate('N')
    assert rover.is_valid_coordinate('E')
    assert rover.is_valid_coordinate('S')
    assert rover.is_valid_coordinate('W')
    assert not rover.is_valid_coordinate('X')


