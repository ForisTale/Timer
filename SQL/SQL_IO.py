import sqlite3
import os


class Database:
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

    def load(self, database="timer.db", file_path=os.getcwd() + "\\"):
        """This method will load database into two dictionaries
        database need to be string with file name
        file_path need to be string with path to database file
        return all tables from database as {table:[list of row as dict]} into
        variable table_dict"""
        self.tables_dict = {}
        con = sqlite3.connect(file_path + database)
        con.row_factory = sqlite3.Row
        cur = con.cursor()

        # get all table names from database
        cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        table_names = []
        table = cur.fetchone()
        while table:
            table_names.append(table[0])
            table = cur.fetchone()
        table_names = tuple(table_names)

        # load tables into {table:[list of row as dict]} and save to table_dict
        for table_name_index in range(len(table_names)):
            cur.execute("SELECT * FROM {}".format(table_names[table_name_index]))
            table_list = []

            timers = cur.fetchone()
            while timers:
                table_list.append(dict(zip(timers.keys(), timers)))
                timers = cur.fetchone()

            self.tables_dict[table_names[table_name_index]] = table_list
        con.close()

    def save(self, database="timer.db", file_path=os.getcwd() + "\\"):
        """This method will save changes in database into file
        """
        con = sqlite3.connect(file_path + database)
        con.row_factory = sqlite3.Row
        cur = con.cursor()

        if self.new_entry:
            for key, value in self.new_entry.items():
                for item in value:
                    keys = []
                    values = []
                    for k in item.keys():
                        keys.append(k)
                        values.append(item[k])
                    keys = tuple(keys)
                    values = tuple(values)

                    cur.execute(
                        "INSERT INTO {table} {keys} VALUES {values}".format(table=key, keys=keys, values=values))
            self.new_entry = {}

        if self.delete_entry:
            pass

        con.commit()
        con.close()

    def add_entry(self, dictionary):
        """will add entry into new_entry.
        dict need to be send as {table_name:[list of new entry as dict]}

        plan to do: if table name or key in dict don't match names and keys in
        tables_dict then it will raise exception.
                    add possibility of add only part of column,
                    for empty none/null.
        """
        for key, value in dictionary.items():
            if key in self.tables_dict:
                self.new_entry[key] = []
                for item in value:
                    if self.tables_dict[key]:
                        if item.keys() == self.tables_dict[key][0].keys() \
                                or not self.tables_dict[key][0]:
                            if self.check_id(item["id"]):
                                # self.tables_dict[key].append(value)
                                self.new_entry[key].append(item)
                                print("Entry: ", item)
                            else:
                                item["id"] = self.auto_id()
                                print("Whole entry: {}".format(item))
                                self.new_entry[key].append(item)
                        else:
                            print("Column names are not the same as they are" 
                                  "in table.")
                    else:
                        self.new_entry[key].append(item)
                        print("Entry: ", item)

            else:
                print("Table name is incorrect")

        self.save()
        self.load()

    def read(self, limit=0):
        """return table_dict as nice looking string
        """
        string = "Database: "
        for tableName, tableItems in self.tables_dict.items():
            string += "Table: " + tableName + "\n"
            if limit <= len(tableItems):
                for each_table_item in tableItems[-limit:]:
                    for key, value in each_table_item.items():
                        string += key.title() + ": " + str(value) + ", "
                    string += "\n"
            else:
                return ("You want to see more records than we have. Now we have : "
                        + str(len(tableItems)) + " records.")
        return string

    def check_id(self, id_num, id_name="id"):
        """will return true if id is NOT in use
        """
        temp_ids = []
        for key, value in self.tables_dict.items():
            for item in value:
                temp_ids.append(item[id_name])
        if id_num not in temp_ids:
            return True
        else:
            return False

    def auto_id(self):
        """return usable, unique id for tables_dict
        """
        id_num = 0
        while not self.check_id(id_num):
            id_num += 1
        return id_num

    def delete_entry(self, table, id_num):
        """will mark entry for delete
        """
        pass

    def add_column(self, table, column_name, data_type):
        """It will mark, that you want add new column into table.
        To avoid errors use this method separately from other methods and save.
        data_type integer, string/text, none/null, real/float, blob.
        """
        pass

    def update_table(self, table, dictionary):
        """
        dict need to be dict with id key and column_name key that you want edit
        """
