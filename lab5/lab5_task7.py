class kangaroo(object):
	def __init__(self, pouch_contents = []):
		self.pouch_contents = pouch_contents

	def put_in_pouch(self, other):
		self.pouch_contents = other

	def __str__(self):
		return (self, self.pouch_contents)


k1 = kangaroo()
k2 = kangaroo()

kang = k1
roo = k2

kang.put_in_pouch(roo)

print(kang.__str__())
