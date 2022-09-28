import sqlite3

mydb = sqlite3.connect("psql1.db")

mycursor = mydb.cursor()

def Create():
    while True:
        print("\n","\t","--Please enter field to store in database--")
        name=input("Enter your name: ")
        city=input("Enter your city: ")
        sql = "INSERT INTO crud (name,city) VALUES (?, ?)"
        val = (name,city)
        mycursor.execute(sql, val)
        mydb.commit()
        print("\n","--Data saved successfully--")
        x=int(input("1:More user\n2:exit\nSelect option: "))
        if x==2:
              return True

