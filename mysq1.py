import mysql.connector

# con=mysql.connector.connect(host='localhost',user='root',password='root')

# c=con.cursor()

# c.execute('create database mydb')
# print("database created successfully")

con = mysql.connector.connect(
    user="root",
    password="root",      # Change if your password is different
    host="127.0.0.1",
    database="mydb"
)

c = con.cursor()

c.execute('''create table if not exists employee(
empid int primary key,
name varchar(20),
age int,
salary int,
gender varchar(20),
place varchar(20)
)''')

print("Table created successfully")

# c.execute('''
# insert into employee (empid,name,age,salary,gender,place)
# values
# (101,"Arun",23,55000,"male","ekm"),
# (102,"Anu",22,45000,"female","kottayam"),
# (103,"Amal",25,20000,"male","tvm"),
# (104,"Manu",20,35000,"male","kollam"),
# (105,"Arathy",30,60000,"female","ekm")
# ''')
#
# con.commit()
#
# print("Data inserted successfully")

c.execute('select * from employee')
k=c.fetchall()
print(k)

c.execute("select * from employee where empid=101")
t=c.fetchall()
print(t)

c.execute("select name,age from employee where empid=101")
t=c.fetchall()
print(t)