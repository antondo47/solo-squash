# initialize the court dimension and some stuff
from dataclasses import dataclass # this is to generate boilerplate special methods

# court dimension
COURT_WIDTH = 6.4
COURT_LENGTH = 9.75
T_POSITION = (3.2, 5.49) # (x, y) of T position
SHORT_LINE = 5.49 # measure from front wall, y position

# surya 
@dataclass
class TrajectoryPoint:
    frame: int
    t: float         # seconds from start of clip
    court_x: float   # metres, 0 -> 6.4
    court_y: float   # metres, 0 -> 9.75

# anh
@dataclass
class ShotEvent:
    frame: int
    t: float         # seconds after the shot was played
    court_x: float   # where the player hit it from
    court_y: float

