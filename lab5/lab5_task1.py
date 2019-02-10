


import math
class Point(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def getx(self):
		return  self.y
	def gety(self):
		return self.y
	def distance_bw_point(self,a2):
		return math.sqrt((self.getx() -a2.getx())**2 + (self.gety() -a2.gety())**2)

point1 = Point(20,30)
point2 = Point(30,20)
print(point1.getx())
print(point1.gety())
print(point2.getx())
print(point2.gety())

print(point1.distance_bw_point(point2))


