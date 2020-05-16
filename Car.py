from Vector2 import Vector2
from Graphics import Graphics
from Utils import *
import Config

class Car():

    def __init__(self, race, startx, starty):
        self.pos = Vector2(startx, starty)
        self.dir = Vector2(0, 0)
        self.vel = Vector2.random2D()
        self.acc = Vector2(0, 0)
        self.r = 3;
        self.maxspeed = 4 * myrandom() + 3
        self.maxforce = 0.1
        self.color = Config.GREEN

        self.vel.setMag(0.5)
        self.sensorRange = self.r * 10
        self.sensorAngleR = radians(20)
        self.sensorAngleL = radians(-20)
        self.sensorHits = []
        self.race = race

    def checkSensors(self):
        self.sensorHits = []
        dl = self.checkSensor(self.sensorAngleL)
        dr = self.checkSensor(self.sensorAngleR)
        return [dr, dl]

    def checkCollisions(self):
        for w in self.race.walls:
            if doesLineInterceptCircle(w.p1, w.p2, self.pos, self.r):
                return True

        return False

    def checkSensor(self, sensorAngle):
        theta = self.vel.heading() # + radians(90);

        n = Vector2.fromAngle(sensorAngle + theta, 1)
        # n.rotate(theta)
        n.setMag(self.sensorRange)
        v = self.pos.copy()
        v.add(n)
        for w in self.race.walls:
            i = intersect(self.pos, v, w.p1, w.p2)
            if i != None:
                self.sensorHits.append(i)
                d = Vector2.dist(self.pos, i)
                return d

        return None

    def think(self):
        rot = 10
        h = self.vel.heading()
        result = self.checkSensors()
        dR = result[0]
        dL = result[1]
        if dR != None and dL != None:
            self.vel.mult(0.001)
            self.turnLeft(rot)
        elif dR != None:
            self.turnLeft(rot)
        elif dL != None:
            self.turnRight(rot)

        # var a = p5.Vector.random2D();
        # a.setMag(0.1);
        # self.applyForce(a);

    def update(self):
        self.vel.add(self.acc)
        self.vel.limit(self.maxspeed)
        self.pos.add(self.vel)
        self.acc.mult(0)
        self.wrapAround()

    def wrapAround(self):
        if self.pos.x < -self.r:
            self.pos.x = Config.WIDTH + self.r
        if self.pos.y < -self.r:
            self.pos.y = Config.HEIGHT + self.r
        if self.pos.x > Config.WIDTH + self.r:
            self.pos.x = -self.r
        if self.pos.y > Config.HEIGHT + self.r:
            self.pos.y = -self.r

    def draw(self, graphics): 
        self.showSensors(graphics)
        graphics.circle(self.pos.x, self.pos.y, self.r * 2, self.color, 0)

    def showSensors(self, graphics):
        theta = self.vel.heading() # + radians(90)
        # rotate(theta);  

        l = Vector2.fromAngle(self.sensorAngleL + theta, 1)
        l.setMag(self.sensorRange)
        graphics.line (self.pos.x, self.pos.y, self.pos.x + l.x, self.pos.y + l.y, 1, Config.WHITE)

        r = Vector2.fromAngle(self.sensorAngleR + theta, 1)
        r.setMag(self.sensorRange)
        graphics.line (self.pos.x, self.pos.y, self.pos.x + r.x, self.pos.y + r.y, 1, Config.WHITE)

        for sh in self.sensorHits:
            graphics.circle(sh.x, sh.y, 2, Config.RED, 0)

    def turnLeft(self, a):
        self.vel.rotate(radians(-a))

    def turnRight(self, a):
        self.vel.rotate(radians(a))

    # A method that calculates and applies a steering force towards a target
    # STEER = DESIRED MINUS VELOCITY
    def seek(self, target): 
        desired = Vector2.subv(target, self.pos) # A vector pointing from the location to the target
        # Normalize desired and scale to maximum speed
        desired.normalize()
        desired.mult(self.maxspeed)
        # Steering = Desired minus Velocity
        steer = Vector2.subv(desired, self.vel)
        steer.limit(self.maxforce) # Limit to maximum steering force
        self.applyForce(steer)
        return steer

    def applyForce(self, f): 
        self.acc.add(f)
