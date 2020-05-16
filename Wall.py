from Vector2 import Vector2
from Graphics import Graphics
import Config

class Wall():

    def __init__(self, x1, y1, x2, y2):
        self.p1 = Vector2(x1, y1)
        self.p2 = Vector2(x2, y2)

    def draw(self, graphics):
        graphics.line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, 2, Config.WHITE)

