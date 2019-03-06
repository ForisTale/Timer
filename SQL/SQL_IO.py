import sqlite3
import os
import copy

class Database():
	def __init__(self):
		self.tables_dict = {}
		self.load()
		self.new_entry = {}
	
	
	def load(self, database="timer.db", file_path=os.getcwd()+"\\"):
		"""This method will load database into two dictionaries
		database need to be string with file name
		file_path need to be string with path to database file
		return all tables from database as {table:[list of row as dict]} into variable table_dict"""
		con=sqlite3.connect(file_path+database)
		con.row_factory = sqlite3.Row
		cur=con.cursor()
	
	
		#get all table names from database
		cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
		tables = []
		for table in cur.fetchall():
			tables.append(table[0])
		tables = tuple(tables)
	
	
		#load all tables into {table:[list of row as dict]} and save to table_dict
		for tab_ind in range(len(tables)):
			cur.execute("SELECT * FROM {}".format(tables[tab_ind]))
			table_list = []
			timers = cur.fetchall()
			for timer in timers:
				temp={}
				for index in range(len(timer)):
					temp[timer.keys()[index]]=timer[index]
				table_list.append(temp)
			self.tables_dict[tables[tab_ind]]= table_list
	
	
		con.close()
	
	
	
	def save(self, database="timer.db", file_path=os.getcwd()+"\\"):
		"""This method will save database into file
		It takes dict as {table:[list of row as dict]}"""
		con = sqlite3.connect(file_path+database)
		con.row_factory=sqlite3.Row
		cur = con.cursor()
		
		
		
	
		
	def add_entry(self, dict):
		"""will add entry into tables_dict
		dict need to be send as {table_name:[list of new entry as dict]}
		
		plan to do: if table name or key in dict don't match names and keys in tables_dict then it will raise exception.
		"""
		for key, value in dict.items():
			if key in self.tables_dict:
				if check_id(dict):
					self.tables_dict[key].append(value)
					self.new_entry[key].append(value)
				else:
					print("Id need to be unique")
				
			else:
				print("Table name is incorrect")
		
		

	def read(self):
		"""return table_dict as new not connected object
		"""	 
		return copy.deepcopy(self.tables_dict)

	def check_id(self, id):
		"""will return true if id is NOT in use
		"""
		temp_ids = []
		for key, value in self.tables_dict.items():
			for item in value:
				temp_ids.append(item["id"])
		if id not in temp_ids:
			return True
		else:
			return False
		
	def auto_id(self):
		"""return usable, unique id for tables_dict
		"""
		id = 0
		while not self.check_id(id):
			id+=1
		return id
		
	
	
	
	
	
	


















