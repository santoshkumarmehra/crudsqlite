import sqlite3

mydb = sqlite3.connect("psql1.db")

mycursor = mydb.cursor()

def Update():
    print("\n","\t","--Select option--","\n","1:Update by Name","2:Update by City")
    x=int(input("Choose option:"))
    if x==1:
        while True:
            name=input("Which name, you want to update : ")
            mycursor.execute("SELECT * from crud")
            myresult = mycursor.fetchall()
            flag=0
            for a,b in myresult:
                if a==name:
                    New_name=input("Enter new name: ")
                    sql="update crud set name=? where name=?;"
                    # val = (name,city)
                    mycursor.execute(sql, (New_name,name))
                    mydb.commit()
                    print("record updated successfully")
                    flag=1
                    break
            if flag==1:
                # print("hello")
                x=int(input("1:More update\n2:exit\nSelect option: "))
                if x==2:
                    flag=3
                    return True
                else:
                    continue
            elif flag==3:
                break          
            else:
                print("There is no such")

    elif x==2:
        while True:
            mycursor.execute("SELECT * from crud")
            myresult = mycursor.fetchall()
            print("\t","--Please enter your name--")
            name=input("Enter your name: ")
            for a,b in myresult:
                if name==a:
                    city=input("which city, you want to update: ")
                    sql="update crud set city=? where name=?;"
                    val = (city,name)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print("record updated successfully")
                    x=int(input("1:More update\n2:exit\nSelect option: "))
                    if x==2:
                        return True
                    elif x==1:
                        break
            else:
                print("There is no such name")
        
    else:
        print("\t","--Please select correctly--")
        Update()

