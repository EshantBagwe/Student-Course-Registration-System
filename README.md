# Student-Course-Registration-System
CLI_Student Course Registration System_python



🧾 Project Overview
The Student Course Registration System is a command-line interface (CLI) application built using Python and MySQL, designed to handle the essential operations of student registration and course enrollment in an academic setting. The project demonstrates the use of relational databases, data normalization, and modular Python programming to build a robust backend system.

🎯 Key Features
🧑‍🎓 Student Registration: Register new students with basic information like name and email.

📚 Course Management: Add and manage available courses in the system.

📝 Course Enrollment: Enroll registered students into specific courses.

📄 View Enrollments: Display all courses a student is enrolled in using SQL JOIN queries.

❌ Drop Course: Remove a student from a course using enrollment ID.

✅ Secure DB Connection: Uses .env file to manage MySQL credentials securely.

🛠️ Tech Stack
Language: Python 3

Database: MySQL

Libraries Used:

mysql-connector-python for DB connectivity

tabulate for CLI tabular output

python-dotenv for environment variable management

🗃️ Database Design
students

student_id (PK)

name

email

courses

course_id (PK)

course_name

enrollments

enroll_id (PK)

student_id (FK)

course_id (FK)

Relationships:

One student can enroll in multiple courses.

One course can have multiple students.

