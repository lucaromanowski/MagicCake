import sqlite3
import os


#conn = sqlite3.connect('example.db')


# Creating coursor
#c = conn.coursor()


# Creating Table
#c.execute(''' CREATE TABLE stock (date text, trans text, symbol text, qty real, price real)''')

# Creating a row of data
#c.execute("INSERT INTO stock VALUES('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) changes
#conn.save()

# We can close the connection now (if everything we want is saved)
#conn.close()




class Rememberer(object):
	'''
	Class made for db managment 
	'''
	def __init__(self):
		# Create DB
		self.db_name = 'example2.db'
		self.current_dir = os.path.dirname(os.path.realpath(__file__))

		
		self.conn = sqlite3.connect(os.path.join(self.current_dir, self.db_name))
		
		self.c = self.conn.cursor()

		

	
	def create_table(self):
		'''
		Create table
		'''

	
		
		# Creating Table
		self.c.execute(''' CREATE TABLE cakes (name text, protein text, carb text, fat text, kcal text)''')



	def remember_it(self, group):
		'''
		This function gets object, pharse it, and save it to db
		'''

		# Iterate over gropu of cakes
		for cake in group:
			# Creating a row of data
			self.c.execute("INSERT INTO cakes VALUES('2006-01-05','BUY','RHAT',100,35.14)")
		#self.conn.commit()

		# Save (commit) changes
		self.conn.commit()

		# We can close the connection now (if everything we want is saved)
		self.conn.close()
