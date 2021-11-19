import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Info51987",
  database="mydatabase"
)

print(mydb)
mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")

# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# sql = "INSERT INTO book_db (name, release_date, isdn) VALUES (%s, %s, %s)"
# val = ("Java for dummies", "Dec 2003", 2004545)
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")

# ------------------select ----------------------
# mycursor.execute("SELECT * FROM book_db")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)


# ------------------ update ---------------------
sql = "UPDATE book_db SET name = 'Canyon 123' WHERE id = 1 "
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")




