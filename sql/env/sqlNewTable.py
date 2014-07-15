# Create a table and populate it with data


import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

cities = [
		('New York City', 'Northeast'),
	    ('San Francisco', 'West'),
	    ('Chicago', 'Midwest'),
	    ('Houston', 'South'),
	    ('Phoenix', 'West'),
	    ('Boston', 'Northeast'),
	    ('Los Angeles', 'West'),
	    ('Houston', 'South'),
	    ('Philadelphia', 'Northeast'),
	    ('San Antonio', 'South'),
	    ('San Diego', 'West'),
	    ('Dallas', 'South'),
	    ('San Jose', 'West'),
	    ('Jacksonville', 'South'),
	    ('Indianapolis', 'Midwest'),
	    ('Austin', 'South'),
	    ('Detroit', 'Midwest')
	     ]

try:
	c.execute("""CREATE TABLE if not exists regions 
				(city TEXT, region TEXT)
				""")
	c.executemany("insert into regions values(?, ? )", cities)
	c.execute("select * from regions order by region")	
	connection.commit()
except sqlite3.OperationalError, e:
	raise e

rows = c.fetchall()

for r in rows:
	print r[0], r[1]