# http://programarcadegames.com/index.php?lang=nl&chapter=introduction_to_animation
# http://programarcadegames.com/index.php?lang=nl&chapter=controllers_and_graphics
from Utils import *
import Config
from Graphics import Graphics
from Race import Race
import json

class Trainer():

	bestbest = 0
	done = False
	race = None
	graphics = None

	def __init__(self, withGrapics = True):
		self.race = Race(self.callback)
		self.graphics = Graphics()
		if withGrapics:
			self.graphics.init("CarAI Trainer", Config.SIZE)

	def callback(self, gen, avg_score, best_score):
		# line = "Generation\t%d\tAverage Score\t%f\tBest Score\t%f" % (gen, avg_score, best_score) 
		# self.write_log(Config.JSON_FOLDER + "/" + "logfile.txt", line)
		# filename = "car-g%03d-%04d.json" % (gen, best_score * 1000)

		if gen == Config.GENERATIONS:
			self.done = True

	def write_log(self, filename, line):
		with open(filename, "a") as outfile:
			outfile.write(line + "\n")

	def write_file(self, filename, data):
		with open(filename, "w") as outfile:
			outfile.write(data + "\n")

	def run(self):
		# Loop until the user clicks the close button.
		while not self.done:

			self.done = self.graphics.queryEvents()

			# Set the screen background
			self.graphics.fill(Config.BLACK)
			self.graphics.print("FPS: {:.2f}".format(self.graphics.fps()))
	
			# Do physics
			self.race.tick()

			# Draw everything 
			self.race.draw(self.graphics)

			# Update screen
			self.graphics.flip()

		# Exit
		self.graphics.quit()


if __name__ == "__main__":
	app = Trainer(True)
	app.run()
