from models.rover import Rover


def process_command(x_max, y_max, rover_position, instructions):
    """
        Processes the instructions to control the robotic rover on the Cartesian plane.

        Args:
            x_max (int): Maximum x-coordinate of the plateau on Mars.
            y_max (int): Maximum y-coordinate of the plateau on Mars.
            rover_position (str): Initial position of the rover in the format "x y coordinate".
            instructions (str): Sequence of instructions (L, R, and M) for the rover to follow.

        Returns:
            str: Final coordinates and direction of the rover after following the provided instructions.

        Raises:
            ValueError: If the rover's coordinates are outside the limits of the plateau or when the initial direction
                        of the rover is invalid.
            ValueError: If an invalid instruction is found in the provided instructions.
    """
    
    x, y, coordinate = rover_position.split()
    x = int(x)
    y = int(y)

    is_valid_position(x, y, x_max, y_max)

    rover = Rover(x, y, coordinate)

    if not rover.is_valid_coordinate(coordinate):
        raise ValueError("The rover's initial heading is invalid.")

    for instruction in instructions:
        try:
            if instruction == 'L':
                rover.turn_left()
            elif instruction == 'R':
                rover.turn_right()
            elif instruction == 'M':
                rover.move()
        except ValueError:
            raise ValueError(f"Invalid statement, check the character: '{instruction}'")
        
    if not is_valid_position(rover.x, rover.y, x_max, y_max):
        return "The rover left the plateau boundaries while executing the instructions."

    return f"{rover.x} {rover.y} {rover.coordinate}"


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

    if not (0 <= x <= x_max and 0 <= y <= y_max):
        raise ValueError("The rover left the limits of the plateau.")
    return True
