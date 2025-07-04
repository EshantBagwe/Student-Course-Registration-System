import mysql.connector
from tabulate import tabulate
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve variables safely

# Establish MySQL connection using TCP/IP (127.0.0.1 preferred on Windows)
conn = mysql.connector.connect(
host = os.getenv("DB_HOST"),
user = os.getenv("DB_USER"),
password = os.getenv("DB_PASSWORD"),
database = os.getenv("DB_NAME")
)
cursor = conn.cursor()

# Function Definitions
def register_student():
    name = input("Enter Student Name: ")
    email = input("Enter Email: ")
    cursor.execute("INSERT INTO students (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    print("Student registered!")

def add_course():
    name = input("Enter Course Name: ")
    cursor.execute("INSERT INTO courses (course_name) VALUES (%s)", (name,))
    conn.commit()
    print("Course added!")

def view_courses():
    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()
    print(tabulate(courses, headers=["Course ID", "Course Name"], tablefmt="fancy_grid"))

def enroll_course():
    student_id = int(input("Enter Student ID: "))
    course_id = int(input("Enter Course ID: "))
    cursor.execute("INSERT INTO enrollments (student_id, course_id) VALUES (%s, %s)", (student_id, course_id))
    conn.commit()
    print("Student enrolled in course.")

def view_enrollments():
    student_id = int(input("Enter Student ID: "))
    cursor.execute("""
        SELECT e.enroll_id, c.course_name 
        FROM enrollments e 
        JOIN courses c ON e.course_id = c.course_id 
        WHERE e.student_id = %s
    """, (student_id,))
    records = cursor.fetchall()
    print(tabulate(records, headers=["Enrollment ID", "Course Name"], tablefmt="grid"))

def drop_course():
    enroll_id = int(input("Enter Enrollment ID to drop: "))
    cursor.execute("DELETE FROM enrollments WHERE enroll_id = %s", (enroll_id,))
    conn.commit()
    print("Enrollment removed.")

# Menu Interface
def menu():
    while True:
        print("\n Student Course Registration System")
        print("1. Register Student")
        print("2. Add Course")
        print("3. View Courses")
        print("4. Enroll in Course")
        print("5. View Enrollments")
        print("6. Drop Course")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")

        if choice == '1':
            register_student()
        elif choice == '2':
            add_course()
        elif choice == '3':
            view_courses()
        elif choice == '4':
            enroll_course()
        elif choice == '5':
            view_enrollments()
        elif choice == '6':
            drop_course()
        elif choice == '7':
            print("Exiting... Bye!")
            break
        else:
            print("Invalid option. Try again.")

# Run the CLI system
menu()

# Clean up MySQL connection
cursor.close()
conn.close()
