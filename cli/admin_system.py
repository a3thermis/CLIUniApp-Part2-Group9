def admin_system():
    while True:
        print("Admin System(c/g/p/r/s/x):")
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
        elif choice == "x":
            print("Exiting Admin System")
            return
        else:
            print("Invalid choice")