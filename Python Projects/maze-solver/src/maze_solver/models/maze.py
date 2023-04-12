from dataclasses import dataclass
from typing import Iterator
from functools import cached_property
from maze_solver.models.square import Square

# Once again creating an immutable data class to ensure underlying tuple of Square remains unchanged once it is assigned
@dataclass(frozen=True)
class Maze:
    squares: tuple[Square, ...]
    
    # Instances will cooperate with the for loop
    def __iter__(self) -> Iterator[Square]:
        return iter(self.squares)
    
    # Enables the square bracket notation for getting index of squares
    def __getitem__(self, index: int) -> Square:
        return self.squares[index]
    
    # Iterate over the maze to find the max cols and rows index with max(). We add 1 to highest index accounts 
    @cached_property
    def width(self):
        return max(square.column for square in self) + 1
    
    @cached_property
    def height(self):
        return max(square.row for square in self) + 1