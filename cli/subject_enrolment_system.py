from student_system import validate_password

def subject_enrolment_system():
    while True:
        print("Subject Enrolment System(c/e/r/s/x):")
        choice = input("Subject Enrolment System(c/e/r/s/x) ").lower()

        if choice == "c":
            print("Change Password")
            while True:
                new_password = input("Enter new password: ")
                if validate_password(new_password):
                    # Password meets the required format
                    print("Password is valid.")
                    break
                else:
                    # Password does not meet the required format
                    print("New password is invalid.")
        elif choice == "e":
            print("Enrol Subject")
        elif choice == "r":
            print("Remove Subject")
        elif choice == "s":
            print("Show Subjects")    
        elif choice == "x":
            print("Exiting Subject Enrolment System")
            return
        else:
            print("Invalid choice")

subject_enrolment_system()