from enum import IntFlag, auto

# We are implementing enum this time around to do bitwise operations
class  Border(IntFlag):
    EMPTY = 0
    TOP = auto()
    BOTTOM = auto()
    LEFT = auto()
    RIGHT = auto()
    
    @property
    def corner(self) -> bool:
        return self in (
            self.TOP | self.LEFT,
            self.TOP | self.RIGHT,
            self.BOTTOM | self.LEFT,
            self.BOTTOM | self.RIGHT,
        )
    
    @property
    def dead_ends(self) -> bool:
        return self.bit_count() == 3
    
    @property
    def intersections(self) -> bool:
        return self.bit_count() < 2