def subject_enrolment_system():
    while True:
        print("Subject Enrolment System(c/e/r/s/x):")
        choice = input("Subject Enrolment System(c/e/r/s/x) ").lower()

        if choice == "c":
            print("Change Password")
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