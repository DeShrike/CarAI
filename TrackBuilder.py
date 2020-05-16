# http://programarcadegames.com/index.php?lang=nl&chapter=introduction_to_animation
# http://programarcadegames.com/index.php?lang=nl&chapter=controllers_and_graphics
from Utils import *
import Config
from Vector2 import Vector2
from Graphics import Graphics
from Wall import Wall
import json

class TrackBuilder():

	pos = None
	dx = 2
	dy = 2
	done = False
	graphics = None
	walls = []
	prev = None

	def __init__(self, withGrapics = True):
		self.graphics = Graphics()
		if withGrapics:
			self.graphics.init("TrackBuilder", Config.SIZE)
			self.graphics.setKeyCallback(self.keyDown)
			self.graphics.setMouseCallback(self.mouseClick)

	def mouseClick(self, x, y):
		if self.pos == None:
			self.pos = Vector2(x, y)
		else:
			if self.prev == None:
				self.prev = Vector2(x, y)
			else:
				self.walls.append(Wall(self.prev.x, self.prev.y, x, y))
				self.prev = Vector2(x, y)

	def keyDown(self, key):
		if key == "W":
			self.writeTrack()
		if key == "L":
			self.prev = None

	def write_file(self, filename, data):
		with open(filename, "w") as outfile:
			outfile.write(data + "\n")

	def writeTrack(self):
		data = {}

		data["width"] = Config.WIDTH
		data["height"] = Config.HEIGHT

		data["startX"] = self.pos.x
		data["startY"] = self.pos.y

		data["walls"] = [(w.p1.x, w.p1.y, w.p2.x, w.p2.y) for w in self.walls]

		jsondata = json.dumps(data, default=lambda o: o.__dict__)
		print("Writing track to track.json")
		self.write_file("track.json", jsondata)

	def run(self):
		# Loop until the user clicks the close button.
		while not self.done:

			self.done = self.graphics.queryEvents()

			# Set the screen background
			self.graphics.fill(Config.BLACK)
			self.graphics.print("Clock: {}".format(self.graphics.fps()))
	
			# Do physics

			# Draw everything
			self.draw()

			# Update screen
			self.graphics.flip()

		# Exit
		self.graphics.quit()

	def draw(self):
		if self.pos != None:
			self.graphics.circle(self.pos.x, self.pos.y, 3, Config.RED, 0)
		for wall in self.walls:
			wall.draw(self.graphics)


if __name__ == "__main__":
	app = TrackBuilder(True)
	app.run()
