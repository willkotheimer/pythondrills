#1.Correct the below code so that the output should be the version number.
#[Example: SQLite version: 3.6.21]

import csv,sqlite3

con = sqlite3.connect('test.db')
with con:

	cur = con.cursor()    
	cur.execute('select sqlite_version()')

	data = cur.fetchone()

	print "SQLite version: %s" % data

#2.Correct the below program so that it should display the last inserted row id.

#[Expected output: The last Id of the inserted row is 4]

import sqlite3

con = sqlite3.connect('new_db')

with con:

	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS Friends;")    
	cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT);")
	cur.execute("INSERT INTO Friends(Name) VALUES ('Tom');")
	cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca');")
	cur.execute("INSERT INTO Friends(Name) VALUES ('Jim');")
	cur.execute("INSERT INTO Friends(Name) VALUES ('Robert');")
	cur.execute('select last_insert_rowid()')
        id = cur.fetchone()
	print "The last Id of the inserted row is %d" % id 


#3.Correct the below code so that it checks weather database exists or not.

import os
import sqlite3
db_filename = 'todo.db'
db_is_new = not os.path.exists(db_filename)
conn = sqlite3.connect(db_filename)
if db_is_new:
	print 'Need to create schema'
	print 'Creating database'
else:
	print 'Database exists, assume schema does, too.'
conn.close()

#4.If Car is a table already created. What is the key word in place of "XXXX" 
#to be used to display the column names of Cars table?

import sqlite3 as lite
import sys
con = lite.connect('test.db')
with con:    
	cur = con.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS Cars(Id INTEGER PRIMARY KEY, Model TEXT, Make TEXT, Year DATE);")    
	cur.execute("SELECT * FROM Cars")
	for colinfo in cur.description:
		print colinfo

#5.Below program is for creating car's table and inserting values. 
#But some corrections are needed. 
#Correct the errors and execute this code.

import sqlite3 as lite

cars = (
	(1, 'Audi', 52642),
	(2, 'Mercedes', 57127),
	(3, 'Skoda', 9000),
	(4, 'Volvo', 29000),
	(5, 'Bentley', 350000),
	(6, 'Hummer', 41400),
	(7, 'Volkswagen', 21600)
)
con = lite.connect('test.db')
with con: 
	cur = con.cursor()    
	cur.execute("DROP TABLE IF EXISTS Cars")
	cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
	for i in range(len(cars)):
		cur.execute("INSERT INTO Cars(Id,Name,Price) VALUES(?,?,?)",cars[i])

#6.If the question5 is successfully executed then retrieve the data 
#by correcting the below code.

import sqlite3 as lite
con = lite.connect('test.db')
with con:    
	cur = con.cursor()    
	cur.execute("SELECT * FROM Cars")
	rows = cur.fetchall()
	for row in rows:
		print row


#7.Correct the below code. [Note: Question 5 should be successfully executed]

import sqlite3 as lite
con = lite.connect('test.db')    
with con:
	con.row_factory = lite.Row
	cur = con.cursor() 
	cur.execute("SELECT * FROM Cars")
	rows = cur.fetchall()
	for row in rows:
		print "%s %s %s" % (row['Id'], row['Name'], row['Price'])

#8.Correct the below code and it should update the values.

import sqlite3 as lite
import sys
uId = 1
uPrice = 62300 
con = lite.connect('test.db')
with con:
	cur = con.cursor()    
	cur.execute("UPDATE Cars SET Price=? WHERE Id=?", (uPrice, uId))        
	con.commit()
	print "Number of rows updated: %d" % cur.rowcount

#9.Correct the below code so that it displays 
#the metadata info of the cars table.

import sqlite3 as lite
con = lite.connect('test.db')
with con:
	cur = con.cursor()    
	cur.execute("PRAGMA table_info('Cars')")
	data = cur.fetchall()
	for d in data:
		print d[0], d[1], d[2]
