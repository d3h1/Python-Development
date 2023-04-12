from enum import IntEnum, auto

# *We are using enum to automatically assign each member a numeric value in turn
# *We also use null value -- none when a role is not assigned
class Role(IntEnum):
    NONE = 0
    ENEMY = auto()
    ENTRANCE = auto()
    EXIT = auto()
    EXTERIOR = auto()
    REWARD = auto()
    WALL = auto()