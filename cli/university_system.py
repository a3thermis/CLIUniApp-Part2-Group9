# .upper():Convert letters to uppercase
# choice = Store the result in choice*
# "=" assignment operator, assigns the value on the right to the variable on the left 
from student_system import student_system  # Import the student_system function from the student_system module
while True:
    #while: Loop that continues until a break statement is encountered
    print("University System: (A)dmin, (S)tudent, or X to exit?")
    choice = input("University System(A/S/X): ").upper()
#    print("Your choice:", choice)
    if choice == "A":
    # == comparison operator, checks if the value on the left is equal to the value on the right
    #if choice: conditional statement
        print("Admin System(c/g/p/r/s/x):")
    elif choice == "S":
    #elif: Check another condition if previous ones failed
        student_system()  # Call the student_system function
    elif choice == "X":
        print("Thank You!")
        break  # Exit the loop
    else:
        print("Invalid choice. Please try again.")
        #Run when none of the conditions matched
