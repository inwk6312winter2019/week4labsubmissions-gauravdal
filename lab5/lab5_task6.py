class Point(object):
	def __init__(self,x = 0, y = 0):
		self.x = x
		self.y = y
	def __str__(self):
		return "this is a string method"
	def __add__(self, other):
		point_add = Point()
		if (type(other) == tuple):
			point_add.x = self.x + other[0]
			point_add.y = self.y + other[1]
			return point_add
		else:
			point_add.x = self.x + other.x
			point_add.y = self.y + other.y
			return point_add

point1 = Point(1,2)
point2 = (3,4)
print(point1.__str__())
sum1 = point1.__add__(point2)
print(sum1.x)
print(sum1.y)
