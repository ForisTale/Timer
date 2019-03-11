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
		print("Program now start count time.")
		
		
	def end(self):
		"""end time
		"""
		if self.time:
			self.time.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
			print("Program now end count time.")
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
		
	def set_id(self):
		"""alow set id number
		"""
		self.id = input("Please write id number for this session: ")
	
	
	def initialize(self):
		"""start program data
		"""
		text = "Please write command, if need write help for list of commands."
		help = "Commands are: \n\"auto\" for start program automatically.\nCommands for manual usage:\n\"start_time\" for starting time count.\n\"end_time\" for end time count.\n\"comment\" for add coment.\n\"tag\" for add tags.\n\"id\" for chose id number.\n\"read\" for see session entry\n\"save\" for saving session\n\n\"close\" for closing program."
		while True:
			inp = input(text)
			
			if inp=="auto":
				pass
			elif inp=="start_time":
				pass
			elif inp=="end_time":
				pass
			elif inp=="comment":
				pass
			elif inp=="tag":
				pass
			elif inp=="id":
				pass
			elif inp=="read":
				pass
			elif inp=="save":
				pass
			elif inp=="close":
				pass
			elif inp=="help":
				print(help)
			else:
				print("I don't recognise this command, for commands list use \"help\"")
			
			












