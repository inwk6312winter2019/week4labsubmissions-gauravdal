
class Point(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def getx(self):
		return  self.y
	def gety(self):
		return self.y
	def setx(self,x1):
		self.x = x1
		return self.x

	def sety(self, y1):
		self.y = y1
		return self.y
	def distance_bw_point(self,a2):
		return math.sqrt((self.getx() -a2.getx())**2 + (self.gety() -a2.gety())**2)


class Rectangle(Point):
	def __init__(self, width, height, corner):
		self.width = width
		self.height = height
		self.corner = corner

	def find_center(self):
		return (self.corner.getx() + (self.width)/2, self.corner.gety() + (self.height)/2)


	def move_rectangle(self, dx, dy):
		return (self.corner.getx() + self.corner.setx(dx), self.corner.getx() + self.corner.sety(dy))




point1 = Point(0,0)
rec1 = Rectangle(5,4,point1)
print(rec1.find_center())

print(rec1.move_rectangle(5,4))
