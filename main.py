from sql.sql_io import Database
from timer import Timer
from interface import initialize

d = Database()
t = Timer()

initialize(t, d)
