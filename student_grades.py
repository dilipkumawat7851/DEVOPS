
students = {
    "Rahul": "A",
    "Priya": "B",
    "Aman": "C"
}

while True:
    print("\n1. Add Student")
    print("2. Update Grade")
    print("3. Display All Grades")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")

        if name in students:
            print("Student already exists!")
        else:
            grade = input("Enter grade: ").upper()
            students[name] = grade
            print("Student added successfully.")

    elif choice == "2":
        name = input("Enter student name: ")

        if name in students:
            grade = input("Enter new grade: ").upper()
            students[name] = grade
            print("Grade updated successfully.")
        else:
            print("Student not found!")

    elif choice == "3":
        print("\nStudent Grades:")
        for name, grade in students.items():
            print(name, ":", grade)

    elif choice == "4":
        print("Program ended.")
        break

    else:
        print("Invalid choice!")
