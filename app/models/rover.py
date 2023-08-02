class Rover:
    """
        Class representing the robotic rover of NASA.

        Attributes:
            x (int): Current x-coordinate (horizontal) of the rover on the Cartesian plane.
            y (int): Current y-coordinate (vertical) of the rover on the Cartesian plane.
            coordinate (str): Current direction of the rover (cardinal points: 'N', 'E', 'S', or 'W').

        Methods:
            turn_left(self): Turns the rover 90 degrees to the left without changing its position.
            turn_right(self): Turns the rover 90 degrees to the right without changing its position.
            move(self): Moves the rover one unit forward in the direction it is facing.
    """

    x: int = 0
    y: int = 0
    direction: str = "N"

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self):
        direction = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
        dx, dy = direction[self.direction]
        self.x += dx
        self.y += dy

    def move_back(self):
        direction = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
        dx, dy = direction[self.direction]
        self.x -= dx  
        self.y -= dy 

                
    def turn_left(self):
        direction = ('N', 'E', 'S', 'W')
        self.direction = direction[(direction.index(self.direction) - 1) % 4]

    def turn_right(self):
        direction = ('N', 'E', 'S', 'W')
        self.direction = direction[(direction.index(self.direction) + 1) % 4]

    

    def is_valid_coordinate(self, direction):
        return direction in ['N', 'E', 'S', 'W']
