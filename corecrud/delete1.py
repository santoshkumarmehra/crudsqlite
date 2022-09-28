import sqlite3

mydb = sqlite3.connect("psql1.db")

mycursor = mydb.cursor()

def Delete():
    while True:
        print("\n","\t","--Select option--","\n","1:Delete by Name","2:Delete by City")
        x=input("Choose option:")
        if x=='1':
            name=input("Which name, You want to delete: ")
            sql="DELETE from crud where name=%s;"
            mycursor.execute(sql, (name,))
            mydb.commit()
            print("record deleted successfully")
            x=int(input("1:Delete more user\n2:exit\nSelect option: "))
            if x==2:
                return True
        elif x=='2':
            city=input("Choose city: ")
            sql="DELETE from crud where city=%s;"
            mycursor.execute(sql, (city,))
            mydb.commit()
            print("record deleted successfully")
            x=int(input("1:Delete more user\n2:exit\nSelect option: "))
            if x==2:
                return True
        else:
            print("\t","--Please select correctly--")
            Delete()

