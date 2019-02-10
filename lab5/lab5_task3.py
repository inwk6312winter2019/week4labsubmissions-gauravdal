

class Time(object):
	def __init__(self,hours,minute,seconds):
		self.hours = hours
		self.minute = minute
		self.seconds = seconds
	def print_time(self):
		print("{:02}:{:02}:{:02}" .format(self.hours,self.minute,self.seconds))

time1 = Time(2,4,7)
time1.print_time()
