from sql.sql_io import Database
from timer import Timer
from interface import Interface


Interface(Timer(), Database()).initialize()
