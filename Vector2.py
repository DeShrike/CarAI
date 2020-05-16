import math
import random

DEG_TO_RAD = math.pi / 180.0
RAD_TO_DEG = 180.0 / math.pi

class Vector2:
	x = 0
	y = 0
	z = 0

	def __init__(self, xx, yy, zz = 0):
		self.x = xx
		self.y = yy
		self.z = zz

	def mag(self):
		return math.sqrt(self.magSq())

	def copy(self):
		return Vector2(self.x, self.y, self.z)

	def dist(self, v):
		return v.copy().sub(self.x, self.y, self.z).mag()

	def magSq(self):
		return self.x * self.x + self.y * self.y + self.z * self.z

	def normalize(self):
		l = self.mag();
		if l != 0:
			self.mult(1.0 / l, 1.0 / l, 1.0 / l)

		return self

	def add(self, x, y = None, z = 0):
		if y == None:
			if isinstance(x, int) or isinstance(x, float):
				self.x += x
				self.y += x
				self.z += x
			else:
				self.x += x.x
				self.y += x.y
				self.z += x.z
		else:
			self.x += x
			self.y += y
			self.z += z
		return self

	def sub(self, x, y = None, z = 0):
		if y == None:
			if isinstance(x, int) or isinstance(x, float):
				self.x -= x
				self.y -= x
				self.z -= x
			else:
				self.x -= x.x
				self.y -= x.y
				self.z -= x.z
		else:
			self.x -= x
			self.y -= y
			self.z -= z
		return self

	def mult(self, x, y = None, z = 0):
		if y == None:
			if isinstance(x, int) or isinstance(x, float):
				self.x *= x
				self.y *= x
				self.z *= x
			else:
				self.x *= x.x
				self.y *= x.y
				self.z *= x.z
		else:
			self.x *= x
			self.y *= y
			self.z *= z
		return self

	def div(self, x, y = None, z = 0):
		if y == None:
			if isinstance(x, int) or isinstance(x, float):
				self.x /= x
				self.y /= x
				self.z /= x
			else:
				self.x /= x.x
				self.y /= x.y
				self.z /= x.z
		else:
			self.x /= x
			self.y /= y
			self.z /= z
		return self

	def setMag(self, n):
		return self.normalize().mult(n, n, n)

	def heading(self):
		return math.atan2(self.y, self.x)

	def rotate(self, a):
		newHeading = self.heading() + a
		# if (this.p5) 
		# newHeading = Vector2.toRadians(newHeading)
		mag = self.mag()
		self.x = math.cos(newHeading) * mag
		self.y = math.sin(newHeading) * mag
		return self

	def limit(self, max):
		mSq = self.magSq()
		if mSq > max * max:
			self.div(math.sqrt(mSq)).mult(max)
		return self

	@staticmethod
	def fromRadians(angle):
		return angle * RAD_TO_DEG

	@staticmethod
	def toRadians(angle):
		return angle * DEG_TO_RAD

	@staticmethod
	def fromDegrees(angle):
		return angle * DEG_TO_RAD

	@staticmethod
	def toDegrees(angle):
		return angle * RAD_TO_DEG

	@staticmethod
	def fromAngle(angle, length):
		return Vector2(length * math.cos(angle), length * math.sin(angle), 0)

	@staticmethod
	def addv(v1, v2):
		target = Vector2(v1.x, v1.y, v1.z)
		target.add(v2)
		return target

	@staticmethod
	def subv(v1, v2):
		target = Vector2(v1.x, v1.y, v1.z)
		target.sub(v2.x, v2.y, v2. z)
		return target

	@staticmethod
	def multv(v1, v2):
		target = Vector2(v1.x, v1.y, v1.z)
		target.mult(v2)
		return target

	@staticmethod
	def divv(v1, v2):
		target = Vector2(v1.x, v1.y, v1.z)
		target.div(v2)
		return target

	@staticmethod
	def random2D():
		target = Vector2(random.random(), random.random(), 0)
		target.normalize()
		return target
