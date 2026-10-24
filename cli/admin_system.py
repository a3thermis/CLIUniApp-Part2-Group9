from database import Database

def admin_system():
    database = Database()
    while True:
        choice = input("Admin System(c/g/p/r/s/x) ").lower()

        if choice == "c":
            print("Clear Database")
        elif choice == "g":
            print("Group Students")
        elif choice == "p":
            print("Partition Students")
        elif choice == "r":
            print("Remove Student")
        elif choice == "s":
            print("Show Students")
            records = database.load_data()

            if not records:
                print("No students found.")
            else:
                for record in records:
                    print("Student ID:", record['student_id"'])
                    print("Name:", record["name"])
                    print("Email:", record["email"])
                    print("Subjects:", record["subjects"])    
        elif choice == "x":
            print("Exiting Admin System")
            return
        else:
            print("Invalid choice")