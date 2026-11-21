import mysql.connector
import re
# create database
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="custodio",
    password="1997",
    database="list_persons"
)
print(mydb)

mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE list_persons")

mycursor.execute("USE list_persons")
#mycursor.execute("CREATE TABLE person (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255),cpf VARCHAR(255))")
mycursor.execute("SHOW TABLES")
for table in mycursor:
    print(table)
#create list_persons

def validate_name(name):
   return bool(name.strip())

def validate_email(email):
   pattern=r'^[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}$'
   return bool(re.fullmatch(pattern, email))


def createPersonsList():

    name=input("Enter a name!\n")
    email = input("Enter a email!\n")
    cpf = input("Enter a cpf")

    if not validate_name(name):
       print("Invalid name!")
       return
     
    if not validate_email(email):
       print("Invalid email!")
       return
     
   

    sql ="INSERT INTO person (name,email,cpf) VALUES (%s,%s,%s)"
    values = [name,email,cpf]
    mycursor.execute(sql, values,)
    mydb.commit()
      

     

def showListPersons():
   mycursor.execute("SELECT id,name,email,cpf FROM  person")
   myresult = mycursor.fetchall()
   for x in myresult:
      print(x)

def searchItemList():
   sql="SELECT * FROM person WHERE id  = %s"
   id = int(input("Enter a id: "))
   value = [id]
   mycursor.execute(sql, value)
   myresult = mycursor.fetchall()
   for x in myresult:
      print(x)

def deletePerson():
   sql = "DELETE FROM person WHERE id = %s"
   id = int(input("Enter a id you like delete!\n"))
   values = [id]
   mycursor.execute(sql,values)
   mydb.commit()

while True:
   print("1.Add list in Persons!")
   print("2.Show the list persons!")
   print("3.Search item in list!")
   print("4.Delete item from the list!")
   print("0.Exit the program1")
   choice = input("Choose 0 a 2!\n")

   if choice == "0":
      print("Bye! Exit the programn!")
      break
   elif choice == "1":
      createPersonsList()

   elif choice == "2":
      showListPersons()

   elif choice == "3":
      searchItemList()

   elif choice == "4":
      deletePerson()
      