import sqlite3
import os

class Database():

	def load(self, database="timer.db", file_path=os.getcwd()+"\\"):
		"""This method will load database into two dictionaries
		database need to be string with file name
		file_path need to be string with path to database file
		return all tables from database as {table:[list of row as dict]}"""
		con=sqlite3.connect(file_path+database)
		con.row_factory = sqlite3.Row
		cur=con.cursor()
		tables_dict = {}
	
	
		#get all table names from database
		cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
		tables = []
		for table in cur.fetchall():
			tables.append(table[0])
		tables = tuple(tables)
	
	
		#load all tables into {table:[list of row as dict]}
		for tab_ind in range(len(tables)):
			cur.execute("SELECT * FROM {}".format(tables[tab_ind]))
			table_list = []
			timers = cur.fetchall()
			for timer in timers:
				temp={}
				for index in range(len(timer)):
					temp[timer.keys()[index]]=timer[index]
				table_list.append(temp)
			tables_dict[tables[tab_ind]]= table_list
	
	
		con.close()
		return tables_dict
	
	
	
	def save(self, tables_dict, database="timer.db", file_path=os.getcwd()+"\\"):
		"""This method will save database into file
		It takes dict as {table:[list of row as dict]}"""
		con = sqlite3.connect(file_path+database)
		con.row_factory=sqlite3.Row
		cur = con.cursor()
	
	























