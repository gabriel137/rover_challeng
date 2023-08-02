from app.models.rover import Rover
import pytest

def test_turn_left():
    """
    Test the turn_left() method of the Rover class.

    This function creates a new Rover object with coordinates (0, 0) and facing 'N'.
    It then calls the turn_left() method on the rover object.
    Finally, it asserts that the rover's coordinate is now 'W'.

    This test ensures that the turn_left() method correctly updates the rover's coordinate when it is facing 'N'.

    Parameters:
        None

    Returns:
        None
    """
    rover = Rover(0, 0, 'N')
    rover.turn_left()
    assert rover.coordinate == 'W'

def test_turn_right():
    """
    Test the turn_right() method of the Rover class.

    This test case verifies that the turn_right() method of the Rover class correctly
    updates the coordinate attribute when the rover turns right. 

    Parameters:
    None

    Returns:
    None
    """
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
    """
    Test the move() method of the Rover class.

    Parameters:
    - initial_x (int): The initial x-coordinate of the rover.
    - initial_y (int): The initial y-coordinate of the rover.
    - initial_direction (str): The initial direction of the rover.
    - expected_x (int): The expected x-coordinate of the rover after moving.
    - expected_y (int): The expected y-coordinate of the rover after moving.

    Returns:
    None
    """
    rover = Rover(initial_x, initial_y, initial_direction)
    rover.move()
    assert rover.x == expected_x
    assert rover.y == expected_y

def test_is_valid_coordinate():
    """
    Test the `is_valid_coordinate` method of the `Rover` class.

    This function creates a `Rover` object at coordinate (0, 0) with a facing direction of 'N'.
    It then asserts that the `is_valid_coordinate` method returns True for the directions 'N', 'E',
    'S', and 'W', and False for the direction 'X'.

    Parameters:
    - None

    Returns:
    - None
    """
    rover = Rover(0, 0, 'N')
    assert rover.is_valid_coordinate('N')
    assert rover.is_valid_coordinate('E')
    assert rover.is_valid_coordinate('S')
    assert rover.is_valid_coordinate('W')
    assert not rover.is_valid_coordinate('X')


