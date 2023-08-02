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
    coordinate: str = "N"

    def __init__(self, x, y, coordinate):
        self.x = x
        self.y = y
        self.coordinate = coordinate

    def move(self):
        coordinate = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
        dx, dy = coordinate[self.coordinate]
        self.x += dx
        self.y += dy

    def move_back(self):
        coordinate = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
        dx, dy = coordinate[self.coordinate]
        self.x -= dx  
        self.y -= dy 

                
    def turn_left(self):
        coordinate = ('N', 'E', 'S', 'W')
        self.coordinate = coordinate[(coordinate.index(self.coordinate) - 1) % 4]

    def turn_right(self):
        coordinate = ('N', 'E', 'S', 'W')
        self.coordinate = coordinate[(coordinate.index(self.coordinate) + 1) % 4]

    

    def is_valid_coordinate(self, coordinate):
        return coordinate in ['N', 'E', 'S', 'W']
