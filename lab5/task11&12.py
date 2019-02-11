class ipaddress(object):

	def __init__ (self, ipaddr, mask):
		self.ipaddr_list =  ipaddr.split(".")
		self.mask_list = '.'.join([str((0xffffffff << (32 - mask) >> i) & 0xff) for i in [24, 16, 8, 0]])
		self.mask_list =  self.mask_list.split(".")
		self.network_list = []
		self.wildcard_list = []
		self.broadcast_list = []
		self.host_min = []
		self.host_max = []
	#ClassA = range(1,127)
	#ClassB = range(127, 192)
	#ClassC = range(192, 224)
	
	
	
	def get_ipaddress(self):
		return ".".join(self.ipaddr_list)

	def get_mask(self):
		return ".".join(self.mask_list)
		
	def get_wildcard(self):
		for octet in self.mask_list:
			temp = 255 - int(octet)
			self.wildcard_list.append(str(temp))
		return ".".join(self.wildcard_list)
	
	def get_network(self):
		for index1 in range(0,len(self.ipaddr_list)):
			for index2 in range(0, len(self.mask_list)):
				if(index1 == index2):
					self.network_list.append(str(int(self.ipaddr_list[index1]) & int(self.mask_list[index2])))
			
		return ".".join(self.network_list)
	
	def get_broadcast(self):
		for index1 in range(0, len(self.network_list)):
			for index2 in range(0, len(self.wildcard_list)):
				if(index1 == index2):
					self.broadcast_list.append(str(int(self.network_list[index1]) | int(self.wildcard_list[index2])))
		
		return ".".join(self.broadcast_list)
		
	def get_host_min(self):
		for index1 in range(0, len(self.network_list)):
			if(index1 == 3):
				self.network_list[index1] = str(int(self.network_list[index1]) + 1)
				self.host_min.append(self.network_list[index1])
			else:
				self.host_min.append(self.network_list[index1])
		
		return ".".join(self.host_min)
	
	def get_host_max(self):
		for index1 in range(0, len(self.broadcast_list)):
			if(index1 == 3):
				self.broadcast_list[index1] = str(int(self.broadcast_list[index1]) -1)
				self.host_max.append(self.broadcast_list[index1])
			else:
				self.host_max.append(self.broadcast_list[index1])
			
		return ".".join(self.host_max)

		
	
	def convert_ip_to_bin(self):
		self.ipaddress_bin = []
		for octet in self.ipaddr_list:
			self.ipaddress_bin.append(format(int(octet), "08b"))
			
		return self.ipaddress_bin
	
	def convert_mask_to_bin(self):
		self.mask_bin = []
		for octet in self.mask_list:
			self.mask_bin.append(format(int(octet), "08b"))
		
		return self.mask_bin
	
	
		
		

ipaddress1 = ipaddress("172.16.65.18",18)

print("ipaddress is :",ipaddress1.get_ipaddress())
print("Mask of the network is :",ipaddress1.get_mask())
print("Wildcard mask is :",ipaddress1.get_wildcard())
print("network of the subnet is :",ipaddress1.get_network())
print("Broadcast address of the subnet is :",ipaddress1.get_broadcast())
print(ipaddress1.get_host_min())
print(ipaddress1.get_host_max())