# SELECT statement


import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	#use a for loop to iterate through the database, printing the results line by line
	c.execute("select firstname, lastname from employees")
	
	# fetchall() retrieves all records from the query
	rows = c.fetchall()

	for r in rows:
		print r[0], r[1]