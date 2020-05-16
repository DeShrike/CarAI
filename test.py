# http://programarcadegames.com/index.php?lang=nl&chapter=introduction_to_animation
# http://programarcadegames.com/index.php?lang=nl&chapter=controllers_and_graphics
from Utils import *
import Config
from Vector2 import Vector2
from Graphics import Graphics
import json

class Test():
	bestbest = 0
	done = False
	graphics = None

	def __init__(self, withGrapics = True):
		self.graphics = Graphics()
		if withGrapics:
			self.graphics.init("Testing", Config.SIZE)

	def run(self):
		# Loop until the user clicks the close button.
		while not self.done:

			self.done = self.graphics.queryEvents()

			# Set the screen background
			self.graphics.fill(Config.BLACK)
			self.graphics.print("Clock: {}".format(self.graphics.fps()))
	
			# Do physics
			doStuff(self.graphics)

			# Update screen
			self.graphics.flip()

		# Exit
		self.graphics.quit()

pos = Vector2(100, 100)
dx = 2
dy = 2

def doStuff(graphics):
	global dx, dy, pos
	r = 20
	p1 = Vector2(50, 50)
	p2 = Vector2(50, 250)
	p3 = Vector2(500, 50)
	p4 = Vector2(500, 250)

	graphics.line(p1.x, p1.y, p4.x, p4.y, 1, Config.WHITE)
	graphics.line(p2.x, p2.y, p3.x, p3.y, 1, Config.WHITE)

	i = intersect(p1, p4, p2, p3)
	if i != None:
		graphics.circle(i.x, i.y, 3, Config.RED, 3)
	i1 = doesLineInterceptCircle(p1, p4, pos, r)
	i2 = doesLineInterceptCircle(p2, p3, pos, r)
	graphics.circle(pos.x, pos.y, r, Config.GREEN if i1 == False and i2 == False else Config.RED, 1)

	pos.x += dx
	pos.y += dy

	if pos.x + r > Config.WIDTH:
		dx *= -1

	if pos.y + r > Config.HEIGHT:
		dy *= -1

	if pos.x - r < 0:
		dx *= -1

	if pos.y - r < 0:
		dy *= -1

if __name__ == "__main__":
	app = Test(True)
	app.run()
