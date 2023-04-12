from dataclasses import dataclass
from typing import Iterator
from functools import cached_property

from maze_solver.models.role import Role
from maze_solver.models.square import Square

# Once again creating an immutable data class to ensure underlying tuple of Square remains unchanged once it is assigned
@dataclass(frozen=True)
class Maze:
    squares: tuple[Square, ...]
    
    # next() calls on GENERATOR EXPRESSIONS that filters squares by their role. Since they were validated, you can now assume that no exceptions will be raised
    @cached_property
    def entrance(self) -> Square:
        return next(sq for sq in self if sq.role is Role.ENTRANCE)
    
    @cached_property
    def exit(self) -> Square:
        return next(sq for sq in self if sq.role is Role.EXIT)
    
    def __post_init__(self) -> None:
        validate_indices(self)
        validate_rows_columns(self)
        validate_entrance(self)
        validate_exit(self)

# ! BOTH FUNCTIONS USE ASSERT to raise assertion error whilst preventing maze from being created with invalid data found
# Checks index prop of each square and if it fits into a continuous sequence of numbers that enumerate all the squares in the maze
def validate_indices(maze: Maze) -> None:
    assert [square.index for square in maze] == list(
        range(len(maze.squares))
    ), 'Wrong square index'
    
# Iterates over rows and columns of maze ensuring that attributes of corresponding square match up with currents of the loop
def validate_rows_columns(maze: Maze) -> None:
    for y in range(maze.height):
        for x in range(maze.width):
            square = maze[y * maze.width + 1]
            assert square.row == y, 'Wrong square.row'
            assert square.column == x, 'Wrong square.column'

# These functions count number of squares whose role are either Entrance and Exit to verify only one of each
def validate_entrance(maze: Maze) -> None:
    assert 1 == sum (
        1 for square in maze if square.role is Role.ENTRANCE
    ), 'Must be exactly one entrance'
    
def validate_exit(maze: Maze) -> None:
    assert 1 == sum (
        1 for square in maze if square.role is Role.EXIT
    ), 'Must be exactly one exit'
    