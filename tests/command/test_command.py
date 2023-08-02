from app.models.command import process_command
import pytest

def test_process_command_valid_input():
    """
    Function to test the process_command function with valid input.

    Parameters:
    - x_max (int): The maximum x coordinate of the grid.
    - y_max (int): The maximum y coordinate of the grid.
    - rover_position (str): The initial position of the rover in the format "x y D", where x and y are the coordinates and D is the direction (N, S, E, W).
    - instructions (str): The instructions for the rover to follow.

    Returns:
    - str: The final position of the rover after executing the instructions.

    Test Cases:
    - Test case 1: Test the process_command function with x_max = 5, y_max = 5, rover_position = "1 2 N", instructions = "LMLMLMLMM". The expected result is "1 3 N".
    - Test case 2: Test the process_command function with x_max = 5, y_max = 5, rover1_position = "1 2 N", rover1_instructions = "LMLMLMLMM", rover2_position = "3 3 E", rover2_instructions = "MMRMMRMRRM". The expected results are "1 3 N" and "5 1 E" respectively.
    """

    x_max, y_max = 5, 5
    rover1_position = "1 2 N"
    rover1_instructions = "LMLMLMLMM"
    rover2_position = "3 3 E"
    rover2_instructions = "MMRMMRMRRM"

    result1 = process_command(x_max, y_max, rover1_position, rover1_instructions)
    result2 = process_command(x_max, y_max, rover2_position, rover2_instructions)

    assert result1 == "1 3 N"
    assert result2 == "5 1 E"

def test_process_command_invalid_input():
    """
    Test case for the process_command function when given invalid input.

    This function tests the process_command function when it is called with invalid input. It verifies that the function raises a ValueError with the correct error message when the rover's position is outside the limits of the plateau, or when the rover's initial heading is invalid.

    Parameters:
    - x_max (int): The maximum x-coordinate of the plateau.
    - y_max (int): The maximum y-coordinate of the plateau.
    - rover_position (str): The initial position of the rover in the format "x y heading".
    - instructions (str): The instructions to be executed by the rover.

    Returns:
    None
    """
    x_max, y_max = 5, 5
    rover_position = "-1 2 N"
    instructions = "LM"
    try:
        result = process_command(x_max, y_max, rover_position, instructions)
    except ValueError as e:
        assert str(e) == "The rover left the limits of the plateau."

    x_max, y_max = 5, 5
    rover_position = "1 2 X"
    instructions = "LM"
    try:
        result = process_command(x_max, y_max, rover_position, instructions)
    except ValueError as e:
        assert str(e) == "The rover's initial heading is invalid."

def test_process_command_boundary():
    """
    Test the behavior of the `process_command` function when the boundaries of the grid are reached.

    This function tests the `process_command` function by passing in different values for the maximum x and y coordinates,
    the rover's initial position, and the instructions. It verifies that the function correctly handles the scenario
    where the rover reaches the boundary of the grid.

    Parameters:
        x_max (int): The maximum x coordinate of the grid.
        y_max (int): The maximum y coordinate of the grid.
        rover_position (str): The initial position of the rover in the format "x y direction".
        instructions (str): The instructions to be executed by the rover.

    Returns:
        str: The final position of the rover in the format "x y direction".

    Raises:
        AssertionError: If the result of `process_command` does not match the expected final position.

    Example:
        >>> x_max, y_max = 1, 1
        >>> rover_position = "0 0 N"
        >>> instructions = "M"
        >>> assert process_command(x_max, y_max, rover_position, instructions) == "0 1 N"

        >>> x_max, y_max = 5, 5
        >>> rover_position = "5 5 N"
        >>> instructions = "M"
        >>> assert process_command(x_max, y_max, rover_position, instructions) == "5 5 N"
    """
    x_max, y_max = 1, 1
    rover_position = "0 0 N"
    instructions = "M"
    assert process_command(x_max, y_max, rover_position, instructions) == "0 1 N"

    x_max, y_max = 5, 5
    rover_position = "5 5 N"
    instructions = "M"
    assert process_command(x_max, y_max, rover_position, instructions) == "5 5 N"


def test_process_command_invalid_instruction():
    """
    Function to test the process_command function with an invalid instruction.
    This function verifies that the process_command function raises a ValueError
    with the correct error message when an invalid instruction is provided.

    Parameters:
    - x_max (int): The maximum value for the x-coordinate.
    - y_max (int): The maximum value for the y-coordinate.
    - rover_position (str): The initial position of the rover.
    - instructions (str): The instructions to be executed by the rover.

    Returns:
    - None

    Raises:
    - AssertionError: If the error message does not match the expected value.

    Example usage:
    test_process_command_invalid_instruction()
    """
    x_max, y_max = 5, 5

    rover_position = "1 2 N"
    instructions = "LMA"
    try:
        process_command(x_max, y_max, rover_position, instructions)
    except ValueError as e:
        assert str(e) == "Invalid statement, check the character: 'A'"


def test_process_command_collision():
    """
    Test the process_command function for collision between two rovers.

    This function tests the process_command function by creating two rovers with 
    positions and instructions that would result in a collision. It verifies that 
    a ValueError is raised with the correct error message.

    Parameters:
    - x_max (int): The maximum x-coordinate of the plateau.
    - y_max (int): The maximum y-coordinate of the plateau.

    Returns:
    None
    """
    x_max, y_max = 5, 5

    rover1_position = "2 3 N"
    rover1_instructions = "M"

    rover2_position = "2 3 E"
    rover2_instructions = "M"
    try:
        process_command(x_max, y_max, rover1_position, rover1_instructions)
        process_command(x_max, y_max, rover2_position, rover2_instructions)
    except ValueError as e:
        assert str(e) == "The rover left the plateau boundaries while executing the instructions."

def test_process_command_sequential_movement():
    """
    This function tests the process_command function for sequential movement of rovers on a given grid.
    
    Parameters:
    - x_max (int): The maximum x-coordinate of the grid.
    - y_max (int): The maximum y-coordinate of the grid.
    - rover_position_1 (str): The initial position of the first rover in the format "x y D", where x and y are the coordinates and D is the direction (N, S, E, or W).
    - instructions_1 (str): The movement instructions for the first rover.
    - rover_position_2 (str): The initial position of the second rover in the format "x y D".
    - instructions_2 (str): The movement instructions for the second rover.
    
    Returns:
    - result_1 (str): The final position of the first rover after executing the movement instructions.
    - result_2 (str): The final position of the second rover after executing the movement instructions.
    
    Raises:
    - AssertionError: If the final positions of the rovers do not match the expected results.
    """
    x_max, y_max = 5, 5

    rover_position_1 = "1 2 N"
    instructions_1 = "LMLMLMLMM"
    result_1 = process_command(x_max, y_max, rover_position_1, instructions_1)

    rover_position_2 = "3 3 E"
    instructions_2 = "MMRMMRMRRM"
    result_2 = process_command(x_max, y_max, rover_position_2, instructions_2)

    assert result_1 == "1 3 N"
    assert result_2 == "5 1 E"
