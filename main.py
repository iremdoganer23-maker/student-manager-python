students = {}

def add_student():
    name = input("Student name: ")
    grade = float(input("Student grade: "))
    students[name] = grade
    print("Student added.")

def list_students():
    if not students:
        print("No students found.")
    else:
        for name, grade in students.items():
            print(name, ":", grade)

def delete_student():
    name = input("Enter student name to delete: ")
    if name in students:
        del students[name]
        print("Student deleted.")
    else:
        print("Student not found.")

while True:

    print("\nSTUDENT MANAGER")
    print("1 - Add Student")
    print("2 - List Students")
    print("3 - Delete Student")
    print("4 - Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        list_students()

    elif choice == "3":
        delete_student()

    elif choice == "4":
        break

    else:
        print("Invalid choice")
