import mysql.connector

# connect to mysql
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

c = con.cursor()

# create database
c.execute("create database if not exists school")

# connect to school database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="school"
)

c = con.cursor()

# create table
c.execute('''
    create table if not exists student(
        roll_no int primary key,
        name varchar(20),
        age int,
        gender varchar(20),
        course varchar(20),
        marks int
    )
''')

print("Table created successfully")


while True:

    print("\n----- STUDENT MENU -----")
    print("1. Insert Student details")
    print("2. Read all student details")
    print("3. Search student by rollno")
    print("4. Update mark of a student")
    print("5. Delete a student record")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # insert
    if choice == 1:

        roll_no = int(input("Enter roll no: "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        gender = input("Enter gender: ")
        course = input("Enter course: ")
        marks = int(input("Enter marks: "))

        c.execute('''
            insert into student
            (roll_no, name, age, gender, course, marks)
            values (%s, %s, %s, %s, %s, %s)
        ''', (roll_no, name, age, gender, course, marks))

        con.commit()

        print("Student details inserted successfully")


    # read all students
    elif choice == 2:

        c.execute("select * from student")

        data = c.fetchall()

        for i in data:
            print(i)


    # search student
    elif choice == 3:

        roll_no = int(input("Enter roll no to search: "))

        c.execute(
            "select * from student where roll_no = %s",
            (roll_no,)
        )

        data = c.fetchone()

        if data:
            print("Roll No:", data[0])
            print("Name:", data[1])
            print("Age:", data[2])
            print("Gender:", data[3])
            print("Course:", data[4])
            print("Marks:", data[5])
        else:
            print("Student not found")


    # update marks
    elif choice == 4:

        roll_no = int(input("Enter roll no: "))
        marks = int(input("Enter new marks: "))

        c.execute(
            "update student set marks = %s where roll_no = %s",
            (marks, roll_no)
        )

        con.commit()

        if c.rowcount > 0:
            print("Marks updated successfully")
        else:
            print("Student not found")


    # delete
    elif choice == 5:

        roll_no = int(input("Enter roll no to delete: "))

        c.execute(
            "delete from student where roll_no = %s",
            (roll_no,)
        )

        con.commit()

        if c.rowcount > 0:
            print("Student deleted successfully")
        else:
            print("Student not found")


    # exit
    elif choice == 6:

        print("Program ended")
        break

    else:
        print("Invalid choice")


c.close()
con.close()