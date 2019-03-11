import datetime



class Timer():
	"""class with purpose to use for measure time
	"""
	def __init__(self):
		self.data = {"timer":[]}
		self.time = []
		self.comments = ""
		self.tags = {"python":0, "sql":0, "ang":0, "jap":0}
		self.id = 0
		
	
	
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
	
	
	def comment(self):
		"""take comment
		"""
		self.comments+=" "+input("Please write comment. ")
	
	def reset_comments(self):
		self.comments = ""
		
	def add_tags(self):
		"""Take input whih tags marks
		"""
		t = ""
		for item in self.tags.keys():
			t+=item+" "
		text = "Please write tags you want separate by space. Tags you can choose are: "+t
		inp = input(text)
		inp = inp.split(" ")
		while True:
			index = 0	
			for item in inp:
				if item in self.tags:
					index+=1
				else:
					print("There is no such tag: "+item)
					inp = input(text)
					inp = inp.split(" ")
					break
			if index == len(inp):
				break
		for item in inp:
			self.tags[item] = 1
				






	def set_data(self):
		"""set all need data into usefull schema
		"""
		if time:
			combine = {"id":self.id, "start":self.time[0], "end":self.time[1], "comment":self.comments, **self.tags}
			self.data["timer"].append(combine)
		else:
			print("Please start time count.")
		
	
	
	
	def initialize(self):
		"""start program data
		"""
		pass













