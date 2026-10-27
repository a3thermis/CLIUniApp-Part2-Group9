from database import Database

def admin_system():
    database = Database()
    while True:
        choice = input("\tAdmin System (c/g/p/r/s/x): ").lower()

        if choice == "c":
            print("\tClearing students database")
            confirm = input("\tAre you sure you want to clear the database (Y)es/(N)o: ").strip().lower()
            if confirm == "y":
                records = database.load_data()
                if not records:
                    print("\tError: Database is already empty.")
                else:
                    database.save_data([])
                    print("\tStudents data cleared.")
        elif choice == "g":
            print("\tGrade Grouping")
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
                print("\t\t< Nothing to Display >")
            else:
                for grade, students in grade_groups.items():
                    print("\t" + grade + " --> [" + ", ".join(students) + "]")
        elif choice == "p":
            print("\tPASS/FAIL Partition")
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
            print("\tPASS --> [" + ", ".join(pass_output) + "]")
        
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
            print("\tFAIL --> [" + ", ".join(fail_output) + "]")
        elif choice == "r":
            records = database.load_data()
            if not records:
                print("\tNo students found.")
            else:
                student_id = input("\tRemove by ID: ")
                found = False
                for record in records:
                    if record["student_id"] == student_id:
                        records.remove(record)
                        database.save_data(records)
                        print("\tRemoving Student", student_id, "Account")
                        found = True
                        break
                if not found:
                    print("\tStudent", student_id, "does not exist")
        elif choice == "s":
            print("\tStudent List")
            records = database.load_data()

            if not records:
                print("\t\t< Nothing to Display >")
            else:
                for record in records:
                    print(
                        "\t" + record["name"] + " :: " + record["student_id"] + " --> Email: " + record["email"])   
        elif choice == "x":
            print("\tExiting Admin System")
            return
        else:
            print("\tInvalid choice")