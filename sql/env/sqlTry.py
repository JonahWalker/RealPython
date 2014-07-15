# INSERT Command with Error Handler


# import the sqlite3 library
import sqlite3

# create the connection object
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
c = conn.cursor()

try:
	# insert data
	c.execute("INSERT INTO populations VALUES('New York', 'NY', 4000)")

	#commit the changes
	conn.commit()
except sqlite3.OperationalError, e:
	raise e

# close the database connection
conn.close()