# http://programarcadegames.com/index.php?lang=nl&chapter=introduction_to_animation
# http://programarcadegames.com/index.php?lang=nl&chapter=controllers_and_graphics
from Utils import *
import Config
from Vector2 import Vector2
from Graphics import Graphics
from Car import Car
import json

class Test2():

	bestbest = 0
	done = False
	graphics = None

	pos1 = None
	vel1 = None
	pos2 = None
	vel2 = None

	extra = 0

	car = None

	def __init__(self, withGrapics = True):
		self.graphics = Graphics()
		if withGrapics:
			self.graphics.init("Testing", Config.SIZE)
			self.graphics.setKeyCallback(self.keyDown)

	def keyDown(self, key):
		if key == "P":
			self.extra += 5
			self.car.turnRight(5)
		elif key == "M":
			self.extra -= 5
			self.car.turnLeft(5)

	def run(self):

		self.setup()

		# Loop until the user clicks the close button.
		while not self.done:

			self.done = self.graphics.queryEvents()

			# Set the screen background
			self.graphics.fill(Config.BLACK)
			self.graphics.print("FPS: {:.2f}".format(self.graphics.fps()))
	
			# Do physics
			self.update()

			# Draw everything
			self.draw()

			# Update screen
			self.graphics.flip()

		# Exit
		self.graphics.quit()

	def setup(self):
		self.pos1 = Vector2(100, 100)
		self.vel1 = Vector2(1, 0) # Vector2.random2D()
		self.vel1.setMag(50)
		self.pos2 = Vector2(200, 100)
		self.vel2 = Vector2.random2D()
		self.vel2.setMag(50)
		self.car = Car(None, 100, 100)

	def update(self):
		self.car.update()

	def draw(self):
		self.draw1(self.pos1, self.vel1, 1)
		self.draw1(self.pos2, self.vel2, 2)
		self.car.draw(self.graphics)

	def draw1(self, pos, vel, ix):
		self.graphics.circle(pos.x, pos.y, 3, Config.RED, 0)
		theta = vel.heading()

		if ix == 1:
			theta += Vector2.toRadians(self.extra)

		l = Vector2.fromAngle(theta, 1)
		if ix == 2:
			l.rotate(Vector2.toRadians(self.extra))
		l.setMag(50)

		self.graphics.print(f"P{ix}: {l.heading():.2f} {Vector2.fromRadians(l.heading()):.2f}°")
		self.graphics.line (pos.x, pos.y, pos.x + l.x, pos.y + l.y, 1, Config.WHITE)


if __name__ == "__main__":
	app = Test2(True)
	app.run()
