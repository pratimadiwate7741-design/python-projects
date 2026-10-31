students = {}

while True:
    print("\n--- STUDENT RECORD MANAGEMENT ---")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display Students")
    print("6. Calculate Average")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = input("Enter Roll Number: ")

        if roll in students:
            print("Student already exists!")
        else:
            name = input("Enter Name: ")
            marks = float(input("Enter Marks: "))
            students[roll] = {"name": name, "marks": marks}
            print("Student added successfully!")

    elif choice == "2":
        roll = input("Enter Roll Number: ")

        if roll in students:
            print(students[roll])
        else:
            print("Student not found!")

    elif choice == "3":
        roll = input("Enter Roll Number: ")

        if roll in students:
            students[roll]["name"] = input("Enter New Name: ")
            students[roll]["marks"] = float(input("Enter New Marks: "))
            print("Record updated!")
        else:
            print("Student not found!")

    elif choice == "4":
        roll = input("Enter Roll Number: ")

        if roll in students:
            del students[roll]
            print("Record deleted!")
        else:
            print("Student not found!")

    elif choice == "5":
        for roll, data in students.items():
            print(roll, data)

    elif choice == "6":
        if students:
            avg = sum(s["marks"] for s in students.values()) / len(students)
            print("Average Marks:", avg)
        else:
            print("No student records available!")

    elif choice == "0":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
