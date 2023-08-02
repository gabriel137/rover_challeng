from app.models.command import process_command
import pytest

def test_process_command_valid_input():
    x_max, y_max = 5, 5
    rover_position = "1 2 N"
    instructions = "LMLMLMLMM"
    result = process_command(x_max, y_max, rover_position, instructions)
    assert result == "1 3 N"

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

# def test_process_command_boundary():
#     x_max, y_max = 1, 1
#     rover_position = "0 0 N"
#     instructions = "M"
#     assert process_command(x_max, y_max, rover_position, instructions) == "0 1 N"

#     x_max, y_max = 5, 5
#     rover_position = "5 5 N"
#     instructions = "M"
#     assert process_command(x_max, y_max, rover_position, instructions) == "5 5 N"


def test_process_command_invalid_instruction():
    x_max, y_max = 5, 5

    rover_position = "1 2 N"
    instructions = "LMA"
    try:
        process_command(x_max, y_max, rover_position, instructions)
    except ValueError as e:
        assert str(e) == "Invalid statement, check the character: 'A'"


def test_process_command_collision():
    x_max, y_max = 5, 5

    # Test collision
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
    x_max, y_max = 5, 5

    # Rover 1
    rover_position_1 = "1 2 N"
    instructions_1 = "LMLMLMLMM"
    result_1 = process_command(x_max, y_max, rover_position_1, instructions_1)

    # Rover 2
    rover_position_2 = "3 3 E"
    instructions_2 = "MMRMMRMRRM"
    result_2 = process_command(x_max, y_max, rover_position_2, instructions_2)

    # Check if the second rover starts moving after the first one has finished
    assert result_1 == "1 3 N"
    assert result_2 == "5 1 E"
