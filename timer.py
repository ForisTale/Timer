import datetime



class Timer():
	"""class with purpose to use for measure time
	"""
	def __init__(self):
		self.data = {"timer":[]}
		self.time = []
		
	
	
	def start(self):
		"""start time
		"""
		self.time = []
		self.time.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		
		
	def end(self):
		"""end time
		"""
		if self.time:
			self.time.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		else:
			print("First use command start.")
	
	def set_data(self):
		"""set all need data into usefull schema
		"""
		pass
	
	