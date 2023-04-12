from typing import NamedTuple, Protocol

# Common interface to all geometric primitives
class Primitive(Protocol):
    def draw(self, **attributes) -> str:
        ...
 
# Returns an SVG Point as a string to define a primitive
class Point(NamedTuple):
    x: int
    y: int
    
    def draw(self, **attributes) -> str:
        return f'{self.x}, {self.y}'

    def translate(self, x=0, y=0) -> 'Point':
        return Point(self.x + x, self.y + y)
    
class Line(NamedTuple):
    start: Point
    end: Point
    
    # Returns an svg line which is standalone
    def draw(self, **attributes) -> str:
        return tag(
            'line',
            x1 = self.x,
            y1 = self.y,
            x2 = self.x,
            y2 = self.y,
            **attributes,
        )

# Open
class Polyline(tuple[Point, ...]):
    def draw(self, **attributes) -> str:
        points = ' '.join(point.draw() for point in self)
        return tag('olyline', points = points, **attributes)

# CLosed
class Polygon(tuple[Point, ...]):
    def draw(self, **attributes) -> str:
        points = ' '.join(point.draw() for point in self)
        return tag('polygon', points = points, **attributes)
    
# Python cannot contain hyphens making us have to find a way to replace the underscores in python names and elements with hyphens so we can read the SVG
def tag(name: str, value: str | None = None, **attributes) -> str:
    attrs = "" if not attributes else " " + " ".join(
        f'{key.replace("_","-")}="{value}"'
        for key, value in attributes.items()
    )
    if value is None:
        return f'<{name}{attrs} />'
    return f'<{name}{attrs}>{value}</{name}>'