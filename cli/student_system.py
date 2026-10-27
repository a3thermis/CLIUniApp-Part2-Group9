from database import Database
from student import Student
import re
import random
#re: Regular expression module for pattern matching
EMAIL_REGEX = r"[^@\s]+@university\.com"
PASSWORD_REGEX = r"[A-Z][A-Za-z]{4,}[0-9]{3,}"
#EMAIL_REGEX: Regular expression pattern to match valid university email addresses
#\.: Match a literal dot character
#PASSWORD_REGEX: Regular expression pattern to match valid passwords
#One uppercase letter
#One uppercase or lowercase letter
#Repeat the preceding element at least four times
#Three digits at the end

def student_system():
    database = Database()
    while True:
#def: Define a function named student_system
        choice = input("\tStudent System (l/r/x): ").lower()
        if choice == "l":
            print("\tStudent Sign In")
            while True:
                Email = input("\tEmail: ")
                Password = input("\tPassword: ")
                if validate_email(Email) and validate_password(Password):
                    print("\temail and password formats acceptable")
                    break
                else:
                    print("\tIncorrect email or password format")
            existing_record = database.find_record_by_email(Email)
            if existing_record is None:
                print("\tStudent does not exist")
            elif existing_record["password"] != Password:
                print("\tIncorrect email or password.")
            else:
                print("\tLogin successful.")
                print("\tWelcome,", existing_record["name"])
                records = database.load_data()
                for record in records:
                    if record["student_id"] == existing_record["student_id"]:
                        existing_record = record
                        break
                from subject_enrolment_system import subject_enrolment_system
                subject_enrolment_system(existing_record)
                database.save_data(records)

        elif choice == "r":
            print("\tStudent Sign Up")
            while True:
                Email = input("\tEnter your university email address: ")
                Password = input("\tPassword: ")
                if validate_email(Email) and validate_password(Password):
                    print("\tEmail and password formats acceptable")
                    break
                else:
                    print("\tIncorrect email or password format")
            existing_record = database.find_record_by_email(Email)
            if existing_record is not None:
                print("\tStudent", existing_record["name"], "already exists")
            else:
                Name = input("\tName: ")
                records = database.load_data()
                student_id = generate_student_id(records)
                new_student = Student(student_id, Name, Email, Password)
                #Create a Student object using the collected registration details.
                new_record = new_student.to_dict()
                #Convert the object into a dictionary suitable for JSON.
                records.append(new_record)
                #Append the new record while retaining existing records.
                database.save_data(records) #the complete updated collection to the file.
                print("\tEnrolling Student", Name)
                print("\tGenerated student ID:", student_id)
        elif choice == "x":
            print("\tExiting Student System.")
            return  # Exit the function
        else:
            print("\tInvalid choice. Please try again.")
def validate_email(email):
    # Check if the email contains '@' and '.'
    if re.fullmatch(EMAIL_REGEX, email):
    #fullmatch: Check if the entire email string matches the EMAIL_REGEX pattern
        return True
    else:
        return False
#True: Boolean value representing truth
#False: Boolean value representing falsehood
def validate_password(password):
    if re.fullmatch(PASSWORD_REGEX, password):
        return True
    else:
        return False
def generate_student_id(records): 
    existing_ids = []
    for record in records: #Load records
        existing_ids.append(record["student_id"])
        #Collect the IDs already stored in the file.
    while True:
        number = random.randint(1, 999999) 
        student_id = str(number).zfill(6)
    #Generate a number,convert it to text, then pad it to six characters.
        if student_id not in existing_ids:
            return student_id


#PASSWORD_REGEX = r"^[A-Z](?=(?:.*[A-Za-z]){4})(?=(?:.*[0-9]){3})[A-Za-z0-9]+"
# (?=(?:.*[A-Za-z]){4}): Check for at least four remaining letters
# (?=(?:.*[0-9]){3}): Check for at least three remaining digits
# [A-Za-z0-9]+: Match one or more letters or digits
# (?=...): Check a condition without consuming characters
# .*： Allow intervening characters
# (?:...): Group part of the pattern
# Check if the email matches the pattern for a valid university email address
#r: Raw string notation to avoid escaping backslashes in the regex pattern
#[^@\s]: Match any character that is not '@' or whitespace