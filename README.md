# 📚 Student Attendance Register

### 🐍 Python Console Application for Classroom Attendance Management

<p align="center">

**Domain:** Python Programming Fundamentals
**Program:** VESA Skill Development Program
**Project:** Project 2 – Student Attendance Register

</p>

---

## 📌 About the Project

The **Student Attendance Register** is a console-based Python application designed to make classroom attendance management simple, organized, and efficient.

The application allows faculty members to:

* 👤 Register students
* 📝 Record daily attendance
* 🔎 Search student records
* 📊 View individual attendance
* 📋 View complete class attendance
* 🧮 Calculate attendance percentages
* ⚠️ Identify students below 75% attendance
* ✏️ Correct the latest attendance record
* 🗑️ Delete student records

The project demonstrates how fundamental Python concepts can be combined to build a practical real-world application.

---

## 🎯 Problem Statement

Managing attendance manually becomes increasingly difficult as the number of students grows.

Tasks such as:

* Maintaining student records
* Recording daily attendance
* Calculating attendance percentages
* Finding individual student records
* Identifying students with low attendance

can require repetitive manual effort.

This project provides a **simple menu-driven command-line solution** to manage student information and attendance records efficiently.

---

## ✨ Key Features

| Feature                   | Description                                              |
| ------------------------- | -------------------------------------------------------- |
| 👤 **Add Student**        | Register students using a unique Roll Number             |
| 📋 **Display Students**   | View all registered students                             |
| 🔎 **Search Student**     | Find a student using their Roll Number                   |
| 📝 **Mark Attendance**    | Record Present (`P`) or Absent (`A`)                     |
| 👤 **Student Attendance** | View detailed attendance of an individual student        |
| 📊 **Class Attendance**   | View attendance statistics for all students              |
| 📈 **Attendance Summary** | Get a quick overview of the latest session               |
| ⚠️ **Low Attendance**     | Identify students below 75% attendance                   |
| 📅 **Today's Attendance** | View present and absent students from the latest session |
| ✏️ **Update Attendance**  | Correct the latest attendance entry                      |
| 🗑️ **Delete Student**    | Remove a student after confirmation                      |

---

## 🎯 Project Objectives

The main objectives of this project are to:

* Maintain student records using unique Roll Numbers.
* Record attendance for multiple students.
* View individual student attendance.
* View complete class attendance.
* Calculate attendance percentages automatically.
* Identify students whose attendance is below **75%**.
* View present and absent students from the latest attendance session.
* Correct the latest attendance record.
* Search and delete student records.
* Keep the application modular and easy to extend.

---

## 🛠️ Technologies Used

| Technology                         | Purpose                                    |
| ---------------------------------- | ------------------------------------------ |
| 🐍 **Python**                      | Core programming language                  |
| 💻 **Command Line / Console**      | User interface                             |
| 📦 **Python Lists & Dictionaries** | Data storage                               |
| 🚫 **No External Libraries**       | Runs using Python's built-in functionality |

---

## 🧠 Python Concepts Demonstrated

This project applies several fundamental Python programming concepts.

### Variables & Data Types

Used for storing:

* Roll Numbers
* Student names
* Attendance values
* Menu choices
* Counts
* Percentages

### Input & Output

The application uses:

```python
input()
```

to accept user information and:

```python
print()
```

to display menus, records, and results.

### Conditional Statements

`if`, `elif`, and `else` are used for:

* Menu selection
* Input validation
* Checking student records
* Attendance calculations
* Low-attendance detection

### Loops

`for` loops are used to process students and attendance records.

A `while` loop keeps the main menu running until the user chooses **Exit**.

### Functions

The application is divided into separate functions for different operations.

Some of the main functions include:

```text
add_student()
display_students()
search_student()
mark_attendance()
view_attendance()
view_all_attendance()
attendance_summary()
low_attendance_students()
today_attendance()
update_attendance()
delete_student()
```

This modular approach makes the program easier to understand, maintain, and extend.

---

## 🗂️ Data Structures

### Lists

Attendance records are stored as lists containing `P` and `A` values.

Example:

```python
["P", "P", "A", "P", "A"]
```

Where:

* `P` = Present
* `A` = Absent

### Dictionaries

Student information is stored using a dictionary.

The **Roll Number** acts as the unique key.

Example:

```python
students = {
    "101": {
        "name": "Rahul",
        "attendance": ["P", "P", "A"]
    }
}
```

---

## 📁 Project Structure

```text
student-attendance-register/
│
├── attendance_register.py
├── README.md
└── .gitignore
```

### File Description

| File                     | Description                    |
| ------------------------ | ------------------------------ |
| `attendance_register.py` | Main Python application        |
| `README.md`              | Project documentation          |
| `.gitignore`             | Specifies files ignored by Git |

---

## ⚙️ Requirements

Before running the project, make sure you have:

* **Python 3.x**
* A terminal or command prompt
* Any code editor such as **VS Code**

No external Python packages are required.

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

Clone or download the repository to your computer.

```bash
git clone <repository-url>
```

Then move into the project directory:

```bash
cd student-attendance-register
```

### 2️⃣ Run the Application

On macOS/Linux:

```bash
python3 attendance_register.py
```

On Windows, you can use:

```bash
python attendance_register.py
```

### 3️⃣ Start Using the Menu

Once the program starts, you will see:

```text
==============================================
       STUDENT ATTENDANCE REGISTER
==============================================
1.  Add Student
2.  Display All Students
3.  Search Student
4.  Mark Attendance
5.  View Student Attendance
6.  View All Students Attendance
7.  Attendance Summary
8.  Low Attendance Students
9.  Today's Attendance
10. Update Attendance
11. Delete Student
12. Exit
==============================================
Enter your choice:
```

---

## 🖥️ Sample Output

### 👤 Adding Students

```text
--- Add Student ---
Enter Roll Number: 101
Enter Student Name: Rahul
Student added successfully.
```

```text
--- Add Student ---
Enter Roll Number: 102
Enter Student Name: Priya
Student added successfully.
```

### 📝 Marking Attendance

```text
========== MARK ATTENDANCE ==========
Enter P for Present and A for Absent.

101 - Rahul (P/A): P
102 - Priya (P/A): A
103 - Aman (P/A): P

Attendance marked successfully.
```

### 📊 Complete Attendance

```text
==================== ATTENDANCE REGISTER ====================
Roll No.  Name                Present   Absent    Total     Percentage
------------------------------------------------------------------------
101       Rahul               2         0         2         100.00%
102       Priya               1         1         2         50.00%
103       Aman                2         0         2         100.00%
```

### ⚠️ Low Attendance Detection

```text
===== STUDENTS BELOW 75% ATTENDANCE =====
Roll No: 102 | Name: Priya | Attendance: 50.00%
```

---

## 📋 Attendance Rules

The application follows these basic rules:

| Input   | Meaning        |
| ------- | -------------- |
| `P`     | Present        |
| `A`     | Absent         |
| `< 75%` | Low Attendance |

Attendance percentage is calculated based on the student's recorded attendance sessions.

---

## 🔐 Assumptions

The application is designed with the following assumptions:

* Every student has a unique Roll Number.
* Attendance is recorded using `P` for Present and `A` for Absent.
* One execution of **Mark Attendance** represents one attendance session/class.
* The latest attendance entry represents the most recent attendance session.
* A **75% attendance threshold** is used for low-attendance detection.
* Student records are stored temporarily in memory during program execution.

---

## 🏗️ Design Approach

The application follows a **modular programming approach**.

Each major operation is implemented as a separate function, while the main program controls the menu and calls the appropriate function based on the user's choice.

### Benefits of this approach

* ✅ Easier to understand
* ✅ Reduces code repetition
* ✅ Simplifies debugging
* ✅ Makes individual features easier to modify
* ✅ Supports future enhancements
* ✅ Improves code readability and maintainability

---

## 🔮 Future Enhancements

The project can be further improved by adding:

* 💾 Permanent data storage using files or a database
* 📅 Date-wise attendance records
* 🔐 Faculty login and authentication
* 📄 Attendance report export to CSV/Excel
* 📊 Monthly attendance reports
* 🔢 Sorting by attendance percentage
* 🖼️ Graphical User Interface (GUI)
* 🏫 Separate classes or sections
* 📑 Automated attendance reports
* 🔄 Backup and restore functionality

---

## 🎓 Learning Outcomes

Through this project, I learned how to apply Python programming fundamentals to a practical problem.

### Key learning outcomes:

* Designing a menu-driven application
* Working with Python lists and dictionaries
* Creating reusable functions
* Validating user input
* Performing calculations using stored data
* Using loops and conditional statements
* Organizing code using modular programming
* Building a practical console-based application

---

## 🏁 Conclusion

The **Student Attendance Register** provides a simple and organized approach to classroom attendance management through a Python console application.

It reduces repetitive manual calculations and provides useful features such as:

**Attendance Recording → Attendance Calculation → Attendance Analysis → Low Attendance Detection**

The project demonstrates how basic Python programming concepts can be combined to create a practical software solution.

---

## 👩‍💻 Author

### **Mrunmayee Tadaskar**

**Python Programming Fundamentals**
**VESA Skill Development Program**

---

<p align="center">

⭐ If you find this project useful, consider giving it a star!

**Built with Python 🐍**

</p>
