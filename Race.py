from Vector2 import Vector2
from Graphics import Graphics
import Config
import json
from Wall import Wall
from Car import Car
from Utils import *

class Race():

    walls = []
    cars = []
    target = None
    startX = None
    startY = None

    def __init__(self, cb):
        self.progress_callback = cb
        self.loadTrack()
        self.setTarget()
        self.ticks = 0

        for i in range(10):
            car = Car(self, self.startX, self.startY)
            self.cars.append(car)

    def setTarget(self):
        x = myrandom(50, Config.WIDTH - 50)
        y = myrandom(50, Config.HEIGHT - 50)
        self.target = Vector2(x, y)
        print(f"Target: {self.target.x},{self.target.y}")

    def read_file(self, filename):
        contents = None
        with open(filename, "r") as infile:
            contents = infile.read()
        return contents

    def loadTrack(self):
        jsondata = self.read_file("tracks/track1.json")
        if jsondata != None:
            data = json.loads(jsondata)
            self.startX = data["startX"]
            self.startY = data["startY"]
            for wall in data["walls"]:
                self.addWall(wall[0], wall[1], wall[2], wall[3])

    def addWall(self, x1, y1, x2, y2):
        w = Wall(x1, y1, x2, y2);
        self.walls.append(w);

    def tick(self):
        self.ticks += 1
        for car in self.cars:
            car.seek(self.target)
            car.think()
            car.update()

        self.progress_callback(1, 1, 1)
        if self.ticks % 100 == 0:
            self.setTarget()

    def draw(self, graphics):
        # print(f"draw {self.target.x} {self.target.y}")
        for wall in self.walls:
            wall.draw(graphics)

        for car in self.cars:
            car.draw(graphics)

        graphics.circle(self.target.x, self.target.y, 4, Config.RED, 0)
        graphics.circle(self.startX, self.startY, 4, Config.GREEN, 0)
