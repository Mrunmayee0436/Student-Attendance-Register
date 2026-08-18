# ============================================================
# Student Attendance Register
# Domain: Python Programming Fundamentals
# Client: STATE Institute of Technology
# ============================================================

students = {}


# ------------------------------------------------------------
# 1. ADD STUDENT
# ------------------------------------------------------------
def add_student():
    print("\n--- Add Student ---")

    roll_number = input("Enter Roll Number: ").strip()

    if not roll_number:
        print("Roll Number cannot be empty.")
        return

    if roll_number in students:
        print("Student with this Roll Number already exists.")
        return

    name = input("Enter Student Name: ").strip()

    if not name:
        print("Student Name cannot be empty.")
        return

    students[roll_number] = {
        "name": name,
        "attendance": []
    }

    print("Student added successfully.")


# ------------------------------------------------------------
# 2. DISPLAY ALL STUDENTS
# ------------------------------------------------------------
def display_students():
    if not students:
        print("\nNo students registered yet.")
        return

    print("\n========== ALL STUDENTS ==========")

    print(f"{'Roll No.':<12}{'Name':<25}")
    print("-" * 37)

    for roll_number, student in students.items():
        print(f"{roll_number:<12}{student['name']:<25}")


# ------------------------------------------------------------
# 3. SEARCH STUDENT
# ------------------------------------------------------------
def search_student():
    print("\n--- Search Student ---")

    roll_number = input("Enter Roll Number: ").strip()

    if roll_number in students:
        student = students[roll_number]

        print("\n--- Student Details ---")
        print(f"Roll Number : {roll_number}")
        print(f"Name        : {student['name']}")

        attendance = student["attendance"]

        if attendance:
            present = attendance.count("P")
            absent = attendance.count("A")
            total = len(attendance)
            percentage = (present / total) * 100

            print(f"Total Classes : {total}")
            print(f"Present       : {present}")
            print(f"Absent        : {absent}")
            print(f"Percentage    : {percentage:.2f}%")
        else:
            print("Attendance   : No records available.")

    else:
        print("Student not found.")


# ------------------------------------------------------------
# 4. MARK ATTENDANCE
# ------------------------------------------------------------
def mark_attendance():
    if not students:
        print("\nNo students registered yet.")
        return

    print("\n========== MARK ATTENDANCE ==========")
    print("Enter P for Present and A for Absent.\n")

    for roll_number, student in students.items():

        while True:
            status = input(
                f"{roll_number} - {student['name']} (P/A): "
            ).strip().upper()

            if status == "P" or status == "A":
                student["attendance"].append(status)
                break
            else:
                print("Invalid input. Please enter only P or A.")

    print("\nAttendance marked successfully.")


# ------------------------------------------------------------
# 5. VIEW INDIVIDUAL ATTENDANCE
# ------------------------------------------------------------
def view_attendance():
    print("\n--- View Student Attendance ---")

    roll_number = input("Enter Roll Number: ").strip()

    if roll_number not in students:
        print("Student not found.")
        return

    student = students[roll_number]
    attendance = student["attendance"]

    print("\n========== ATTENDANCE DETAILS ==========")
    print(f"Roll Number : {roll_number}")
    print(f"Name        : {student['name']}")

    if not attendance:
        print("No attendance records available.")
        return

    present = attendance.count("P")
    absent = attendance.count("A")
    total = len(attendance)
    percentage = (present / total) * 100

    print(f"Total Classes : {total}")
    print(f"Present       : {present}")
    print(f"Absent        : {absent}")
    print(f"Attendance    : {percentage:.2f}%")

    print("\nAttendance Record:")

    for i in range(len(attendance)):
        print(f"Class {i + 1}: {attendance[i]}")


# ------------------------------------------------------------
# 6. VIEW EVERYONE'S ATTENDANCE
# ------------------------------------------------------------
def view_all_attendance():
    if not students:
        print("\nNo students registered yet.")
        return

    print("\n==================== ATTENDANCE REGISTER ====================")

    print(
        f"{'Roll No.':<10}"
        f"{'Name':<20}"
        f"{'Present':<10}"
        f"{'Absent':<10}"
        f"{'Total':<10}"
        f"{'Percentage':<12}"
    )

    print("-" * 72)

    for roll_number, student in students.items():

        attendance = student["attendance"]

        present = attendance.count("P")
        absent = attendance.count("A")
        total = len(attendance)

        if total > 0:
            percentage = (present / total) * 100
        else:
            percentage = 0

        print(
            f"{roll_number:<10}"
            f"{student['name']:<20}"
            f"{present:<10}"
            f"{absent:<10}"
            f"{total:<10}"
            f"{percentage:.2f}%"
        )


# ------------------------------------------------------------
# 7. ATTENDANCE SUMMARY
# ------------------------------------------------------------
def attendance_summary():
    if not students:
        print("\nNo students registered yet.")
        return

    total_students = len(students)

    present_students = 0
    absent_students = 0

    for student in students.values():

        attendance = student["attendance"]

        if attendance:
            if attendance[-1] == "P":
                present_students += 1
            elif attendance[-1] == "A":
                absent_students += 1

    print("\n========== ATTENDANCE SUMMARY ==========")

    print(f"Total Students : {total_students}")
    print(f"Present Today  : {present_students}")
    print(f"Absent Today   : {absent_students}")


# ------------------------------------------------------------
# 8. LOW ATTENDANCE STUDENTS
# ------------------------------------------------------------
def low_attendance_students():
    if not students:
        print("\nNo students registered yet.")
        return

    threshold = 75

    print(f"\n===== STUDENTS BELOW {threshold}% ATTENDANCE =====")

    found = False

    for roll_number, student in students.items():

        attendance = student["attendance"]

        if not attendance:
            continue

        present = attendance.count("P")
        percentage = (present / len(attendance)) * 100

        if percentage < threshold:

            print(
                f"Roll No: {roll_number} | "
                f"Name: {student['name']} | "
                f"Attendance: {percentage:.2f}%"
            )

            found = True

    if not found:
        print("No students have attendance below 75%.")


# ------------------------------------------------------------
# 9. TODAY'S ATTENDANCE
# ------------------------------------------------------------
def today_attendance():
    if not students:
        print("\nNo students registered yet.")
        return

    print("\n========== TODAY'S ATTENDANCE ==========")

    print("\n--- Present Students ---")

    present_found = False

    for roll_number, student in students.items():

        attendance = student["attendance"]

        if attendance and attendance[-1] == "P":
            print(f"{roll_number} - {student['name']}")
            present_found = True

    if not present_found:
        print("No students marked present.")

    print("\n--- Absent Students ---")

    absent_found = False

    for roll_number, student in students.items():

        attendance = student["attendance"]

        if attendance and attendance[-1] == "A":
            print(f"{roll_number} - {student['name']}")
            absent_found = True

    if not absent_found:
        print("No students marked absent.")


# ------------------------------------------------------------
# 10. UPDATE LAST ATTENDANCE
# ------------------------------------------------------------
def update_attendance():
    if not students:
        print("\nNo students registered yet.")
        return

    print("\n--- Update Attendance ---")

    roll_number = input("Enter Roll Number: ").strip()

    if roll_number not in students:
        print("Student not found.")
        return

    attendance = students[roll_number]["attendance"]

    if not attendance:
        print("No attendance record exists for this student.")
        return

    print(f"Current Attendance: {attendance[-1]}")

    while True:

        new_status = input(
            "Enter new status (P = Present, A = Absent): "
        ).strip().upper()

        if new_status == "P" or new_status == "A":
            attendance[-1] = new_status
            print("Attendance updated successfully.")
            break
        else:
            print("Invalid input. Please enter P or A.")


# ------------------------------------------------------------
# 11. DELETE STUDENT
# ------------------------------------------------------------
def delete_student():
    if not students:
        print("\nNo students registered yet.")
        return

    print("\n--- Delete Student ---")

    roll_number = input("Enter Roll Number: ").strip()

    if roll_number not in students:
        print("Student not found.")
        return

    name = students[roll_number]["name"]

    confirmation = input(
        f"Are you sure you want to delete {name}? (Y/N): "
    ).strip().upper()

    if confirmation == "Y":
        del students[roll_number]
        print("Student deleted successfully.")
    else:
        print("Delete operation cancelled.")


# ------------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------------
def main():

    while True:

        print("\n")
        print("==============================================")
        print("       STUDENT ATTENDANCE REGISTER")
        print("==============================================")
        print("1.  Add Student")
        print("2.  Display All Students")
        print("3.  Search Student")
        print("4.  Mark Attendance")
        print("5.  View Student Attendance")
        print("6.  View All Students Attendance")
        print("7.  Attendance Summary")
        print("8.  Low Attendance Students")
        print("9.  Today's Attendance")
        print("10. Update Attendance")
        print("11. Delete Student")
        print("12. Exit")
        print("==============================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            mark_attendance()

        elif choice == "5":
            view_attendance()

        elif choice == "6":
            view_all_attendance()

        elif choice == "7":
            attendance_summary()

        elif choice == "8":
            low_attendance_students()

        elif choice == "9":
            today_attendance()

        elif choice == "10":
            update_attendance()

        elif choice == "11":
            delete_student()

        elif choice == "12":
            print("\nThank you for using Student Attendance Register.")
            print("Program closed successfully.")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 12.")


# ------------------------------------------------------------
# PROGRAM START
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
