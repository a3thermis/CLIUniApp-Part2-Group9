import re
#re: Regular expression module for pattern matching
EMAIL_REGEX = r"[^@\s]+@university\.com"
#EMAIL_REGEX: Regular expression pattern to match valid university email addresses
# Check if the email matches the pattern for a valid university email address
#r: Raw string notation to avoid escaping backslashes in the regex pattern
#[^@\s]: Match any character that is not '@' or whitespace
#\.: Match a literal dot character
def student_system():
    while True:
#def: Define a function named student_system
        print("Student System: (l)ogin, (r)egister, or (x) to exit?")
        choice = input("Student System(l/r/x): ").lower()
        print("Student System(l/r/x):", choice)
        if choice == "l":
            print("Student Sign in")
        elif choice == "r":
            print("Student Sign up")
            Email = input("Enter your university email address: ")
            if validate_email(Email):
                print("Email format accepted.")
            else:
                print("Incorrect email address. Please enter a valid university email address.")
        elif choice == "x":
            print("Exiting Student System.")
            return  # Exit the function
def validate_email(email):
    # Check if the email contains '@' and '.'
    if re.fullmatch(EMAIL_REGEX, email):
    #fullmatch: Check if the entire email string matches the EMAIL_REGEX pattern
        return True
    else:
        return False
#True: Boolean value representing truth
#False: Boolean value representing falsehood