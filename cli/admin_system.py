from database import Database

def admin_system():
    database = Database()
    while True:
        choice = input("Admin System (c/g/p/r/s/x): ").lower()

        if choice == "c":
            print("Clearing students database")
            confirm = input("Are you sure you want to clear the database (Y)es/(N)o: ").strip().lower()
            if confirm == "y":
                records = database.load_data()
                if not records:
                    print("Error: Database is already empty.")
                else:
                    database.save_data([])
                    print("Students data cleared.")
        elif choice == "g":
            print("Grade Grouping")
            records = database.load_data()
            grade_groups = {}
            for record in records:
                average = record["average_mark"]
                if average >= 85:
                    grade = "HD"
                elif average >= 75:
                    grade = "D"
                elif average >= 65:
                    grade = "C"
                elif average >= 50:
                    grade = "P"
                else:
                    grade = "Z"
                if grade not in grade_groups:
                    grade_groups[grade] = []
                grade_groups[grade].append(
                    record["name"] + " :: " + str(record["student_id"]) + 
                    " --> GRADE: " + grade + " - MARK: " + "{:.2f}".format(average)
                )
            if not grade_groups:
                print("    < Nothing to Display >")
            else:
                for grade, students in grade_groups.items():
                    print(grade, " --> [" + ", ".join(students) + "]")
        elif choice == "p":
            print("PASS/FAIL Partition")
            records = database.load_data()
            pass_students = []
            fail_students = []
            for record in records:
                average = record["average_mark"]
                if average >= 50:
                    pass_students.append(record)
                else:
                    fail_students.append(record)         
            pass_output = []
            for record in pass_students:
                average = record["average_mark"]
                if average >= 85:
                    grade = "HD"
                elif average >= 75:
                    grade = "D"
                elif average >= 65:
                    grade = "C"
                elif average >= 50:
                    grade = "P"
                else:
                    grade = "Z"
                pass_output.append(
                    record["name"] + " :: " + str(record["student_id"]) + " --> "
                    + "GRADE: " + grade + " - MARK: " + "{:.2f}".format(average)
                )
            print("PASS --> [" + ", ".join(pass_output) + "]")
        
            fail_output = []
            for record in fail_students:
                average = record["average_mark"]
                if average >= 85:
                    grade = "HD"
                elif average >= 75:
                    grade = "D"
                elif average >= 65:
                    grade = "C"
                elif average >= 50:
                    grade = "P"
                else:
                    grade = "Z"
                fail_output.append(
                    record["name"] + " :: " + str(record["student_id"]) + " --> "
                    + "GRADE: " + grade + " - MARK: " + "{:.2f}".format(average)
                )
            print("FAIL --> [" + ", ".join(fail_output) + "]")
        elif choice == "r":
            records = database.load_data()
            if not records:
                print("No students found.")
            else:
                student_id = input("Remove by ID: ")
                found = False
                for record in records:
                    if record["student_id"] == student_id:
                        records.remove(record)
                        database.save_data(records)
                        print("Removing Student", student_id, "Account")
                        found = True
                        break
                if not found:
                    print("Student", student_id, "does not exist")
        elif choice == "s":
            print("Student List")
            records = database.load_data()

            if not records:
                print("    < Nothing to Display >")
            else:
                for record in records:
                    print(
                        record["name"], "::", record["student_id"], "--> Email:", record["email"])   
        elif choice == "x":
            print("Exiting Admin System")
            return
        else:
            print("Invalid choice")