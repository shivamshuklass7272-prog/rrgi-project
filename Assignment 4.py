import json
from pathlib import Path


FILE_NAME = Path(__file__).with_name("students.json")


class Student:
    def __init__(self, student_id, name, python, sql, mathematics):
        self.student_id = student_id
        self.name = name
        self.python = python
        self.sql = sql
        self.mathematics = mathematics

    def total(self):
        return self.python + self.sql + self.mathematics

    def average(self):
        return self.total() / 3

    def grade(self):
        average = self.average()
        if average >= 90:
            return "A+"
        if average >= 80:
            return "A"
        if average >= 70:
            return "B"
        if average >= 60:
            return "C"
        if average >= 50:
            return "D"
        return "F"

    def to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "python": self.python,
            "sql": self.sql,
            "mathematics": self.mathematics,
        }


def load_data():
    if not FILE_NAME.exists():
        return []

    with FILE_NAME.open("r") as file:
        data = json.load(file)

    students = []
    for item in data:
        if "id" in item:
            students.append(
                Student(
                    item["id"], item["name"], item["python"],
                    item["sql"], item["mathematics"]
                )
            )
        else:
            marks = item["marks"]
            students.append(
                Student(
                    item["student_id"], item["name"], marks["Python"],
                    marks["SQL"], marks["Mathematics"]
                )
            )
    return students


def save_data(students):
    with FILE_NAME.open("w") as file:
        json.dump([student.to_dict() for student in students], file, indent=4)


def print_student(student):
    lines = [
        f"Student ID : {student.student_id}",
        f"Name       : {student.name}",
        f"Python     : {student.python}",
        f"SQL        : {student.sql}",
        f"Mathematics: {student.mathematics}",
        f"Total      : {student.total()}",
        f"Average    : {student.average():.2f}",
        f"Grade      : {student.grade()}",
    ]
    width = max(len(line) for line in lines) + 4
    border = "+" + "-" * width + "+"

    print("\n" + border)
    for line in lines:
        print("| " + line.ljust(width - 2) + " |")
    print(border)


def add_student(students):
    student_id = input("Enter Student ID: ").strip()
    name = input("Enter Student Name: ").strip()

    if not student_id or not name:
        print("Student ID and name are required.")
        return

    if any(student.student_id == student_id for student in students):
        print("Student ID already exists.")
        return

    try:
        marks = [
            float(input("Enter marks for Python: ")),
            float(input("Enter marks for SQL: ")),
            float(input("Enter marks for Mathematics: ")),
        ]
    except ValueError:
        print("Please enter valid marks.")
        return

    if not all(0 <= mark <= 100 for mark in marks):
        print("Marks must be between 0 and 100.")
        return

    student = Student(student_id, name, *marks)
    students.append(student)
    save_data(students)

    print("\nStudent data added:")
    print_student(student)


def display_students(students):
    if not students:
        print("No students found.")
        return

    headers = ["ID", "Name", "Python", "SQL", "Mathematics", "Total", "Average", "Grade"]
    rows = [
        [
            str(student.student_id),
            student.name,
            str(student.python),
            str(student.sql),
            str(student.mathematics),
            str(student.total()),
            f"{student.average():.2f}",
            student.grade(),
        ]
        for student in students
    ]
    widths = [
        max(len(headers[index]), *(len(row[index]) for row in rows)) + 2
        for index in range(len(headers))
    ]
    border = "+" + "+".join("-" * width for width in widths) + "+"

    print("\n" + border)
    print("|" + "|".join(headers[index].center(widths[index]) for index in range(len(headers))) + "|")
    print(border)
    for row in rows:
        print("|" + "|".join(row[index].center(widths[index]) for index in range(len(row))) + "|")
    print(border)


def search_student(students):
    student_id = input("Enter Student ID to search: ").strip()
    student = next(
        (student for student in students if student.student_id == student_id),
        None,
    )
    if student:
        print_student(student)
    else:
        print("Student not found.")


def main():
    students = load_data()

    while True:
        print("\nSTUDENT MANAGEMENT SYSTEM")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            print("Thank you for using Student Management System!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()