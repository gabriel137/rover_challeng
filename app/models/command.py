from .rover import Rover


def process_command(x_max, y_max, rover_position, instructions):
    """
    Process the given command to move a rover on a plateau.

    Parameters:
        x_max (int): The maximum x-coordinate of the plateau.
        y_max (int): The maximum y-coordinate of the plateau.
        rover_position (str): The initial position of the rover (format: "x y direction").
        instructions (str): The instructions for the rover to execute.

    Returns:
        str: The final position of the rover after executing the instructions.

    Raises:
        ValueError: If the rover's initial heading is invalid or if an invalid instruction is encountered.
    """

    x, y, direction = rover_position.split()
    x = int(x)
    y = int(y)

    if not is_valid_position(x, y, x_max, y_max):
        return "The rover left the plateau boundaries while executing the instructions."

    rover = Rover(x, y, direction)

    if not rover.is_valid_direction(direction):
        raise ValueError("The rover's initial heading is invalid.")

    for instruction in instructions:
        try:
            if instruction == 'L':
                rover.turn_left()
            elif instruction == 'R':
                rover.turn_right()
            elif instruction == 'M':
                rover.move()
                if not is_valid_position(rover.x, rover.y, x_max, y_max):
                    rover.move_back()
        except ValueError:
            raise ValueError(f"Invalid statement, check the character: '{instruction}'")

    return f"{rover.x} {rover.y} {rover.direction}"


def is_valid_position(x, y, x_max, y_max):
    """
        Checks if the rover's coordinates are within the limits of the plateau.

        Args:
            x (int): Current x-coordinate of the rover on the Cartesian plane.
            y (int): Current y-coordinate of the rover on the Cartesian plane.
            x_max (int): Maximum x-coordinate of the plateau on Mars.
            y_max (int): Maximum y-coordinate of the plateau on Mars.

        Returns:
            bool: True if the coordinates are within the limits of the plateau; otherwise, an exception is raised.
    """

    return 0 <= x <= x_max and 0 <= y <= y_max