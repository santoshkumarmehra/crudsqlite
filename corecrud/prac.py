import sqlite3

mydb = sqlite3.connect("psql1.db")
mycursor = mydb.cursor()

# cursor = mycursor.cursor()
# print("connected")
# Command="CREATE TABLE crud(name text,city text)"
# mycursor.execute(Command)
# mydb.commit()

# name=input("name: ")
# city=input("city: ")

# mycursor.execute("insert into crud(name,city) values('{}','{}')".format(name,city))
# mydb.commit()

# r="select * from crud"
# fetch = mycursor.execute(r).fetchall()
# for i in fetch:
#     print(i)


