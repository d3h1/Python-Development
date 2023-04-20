from dataclasses import dataclass
from maze_solver.models.border import Border
from maze_solver.models.role import Role

# The frozen class allows these objects to become immutable once the are set because there is no need to change these squares and their variables once set
@dataclass(frozen=True)
class Square:
    index: int
    row: int
    col: int
    border: Border
    role: Role = Role.NONE