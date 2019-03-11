import sqlite3
import os
import copy

class Database():
	"""
	"""
	def __init__(self):
		self.tables_dict = {}
		self.load()
		self.new_entry = {}
		self.delete_entry = {}
	"""
	def __repr__(self):
		return str(self.tables_dict)
	"""
	
	def load(self, database="timer.db", file_path=os.getcwd()+"\\"):
		"""This method will load database into two dictionaries
		database need to be string with file name
		file_path need to be string with path to database file
		return all tables from database as {table:[list of row as dict]} into variable table_dict"""
		self.tables_dict = {}
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
		"""This method will save changes in database into file
		"""
		con = sqlite3.connect(file_path+database)
		con.row_factory=sqlite3.Row
		cur = con.cursor()
		
		if self.new_entry:
			for key, value in self.new_entry.items():
				table = key
				for item in value:
					keys = []
					values = []
					for k in item.keys():
						keys.append(k)
						values.append(item[k])
					keys = tuple(keys)
					values = tuple(values)
					

					cur.execute("INSERT INTO {table} {keys} VALUES {values}".format(table = key, keys = keys, values = values))
		
		if self.delete_entry:
			pass
		
		
		con.commit()
		con.close()
		
	def add_entry(self, dict):
		"""will add entry into new_entry.
		dict need to be send as {table_name:[list of new entry as dict]}
		
		plan to do: if table name or key in dict don't match names and keys in tables_dict then it will raise exception.
					add posibility of add only part of column, for empty none/null
		"""

		for key, value in dict.items():
			if key in self.tables_dict:
				self.new_entry[key]=[]
				for item in value:
					if item.keys()==self.tables_dict[key][0].keys() or not self.tables_dict[key][0]:
						if self.check_id(item["id"]):
							#self.tables_dict[key].append(value)
							self.new_entry[key].append(item)
							print("Entry: ", item)
						else:
							item["id"] = self.auto_id()
							print("Id was used by other row, new unique id wass added. New id is: {}\\nWhole entry now look like: {}".format(item["id"]), item)
							self.new_entry[key].append(item)
					else:
						print("Column names are not the same as they are in table.")
			else:
				print("Table name is incorrect")
		
		self.save()
		self.load()
		

	def read(self):
		"""return table_dict as new not connected object
		"""	 
		return copy.deepcopy(self.tables_dict)

	def check_id(self, id, id_name="id"):
		"""will return true if id is NOT in use
		"""
		temp_ids = []
		for key, value in self.tables_dict.items():
			for item in value:
				temp_ids.append(item[id_name])
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
		
	
	def delete_entry(self, table, id):
		"""will mark entry for delete
		"""
		pass
	
	
	def add_colunm(self, table, column_name, data_type):
		"""It will mark, that you want add new column into table. To save use save method! 
		To avoid errors use this method separetly from other methods and save imedietly.
		data_type integer, string/text, none/null, real/float, blob.
		"""
		pass
	
	def update_table(self, table, dict):
		"""
		dict need to be dict with id key and column_name key that you want edit
		"""

















