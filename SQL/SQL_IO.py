import sqlite3
import os

class Database():
	def __init__(self):
		self.tables_dict = {}
		self.load()
	
	
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
		
		
		
	
		
	def add_entry(self, id, start, end, **kwargs):
		"""will add entry into tables_dict
		unique id, use check_id method or auto_id method 
		start need to be datetime object 
		end need to be datetime object
		kwargs are dict with tags where {tag name: 0 or 1}
		"""
		pass

	def read(self):
		"""return table_dict as new not connected object
		"""
		temp = {}
		for key, value in self.tables_dict.items():
			temp[key]=value
		
		return temp

	def check_id(self, id):
		"""will return true if id is in use
		"""
		pass
		
	def auto_id(self):
		"""return usable, unique id for tables_dict
		"""
		pass
		
	
	
	
	
	
	


















