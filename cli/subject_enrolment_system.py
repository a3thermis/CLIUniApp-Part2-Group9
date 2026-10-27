from student_system import validate_password
from subject import Subject

def subject_enrolment_system(student_record):
    while True:
        choice = input("\tStudent Course Menu (c/e/r/s/x): ").lower()

        if choice == "c":
            print("\tUpdating Password")
            while True:
                new_password = input("\tNew Password: ")
                if validate_password(new_password):
                    while True:
                        confirm_password = input("\tConfirm Password: ")
                        if confirm_password != new_password:
                            print("\tPassword does not match - try again")
                        else:
                            student_record["password"] = new_password
                            print("\tPassword updated successfully.")
                            break
                    break
                else:
                    # Password does not meet the required format
                    print("\tNew password is invalid.")
        elif choice == "e":
            print("\tEnrol a subject")

            if len(student_record["subjects"]) >= 4:
                print("\tYou have reached the 4 subject enrolment limit.")
            else:
                print("\tYou can enrol in a new subject.")
                new_subject = Subject()
                id_exists = False
                for subject in student_record["subjects"]:
                    if subject["subject_id"] == new_subject.subject_id:
                        id_exists = True
                        break
                while id_exists:
                    new_subject = Subject()
                    id_exists = False
                    for subject in student_record["subjects"]:
                        if subject["subject_id"] == new_subject.subject_id:
                            id_exists = True
                            break
                student_record["subjects"].append(new_subject.to_dict()) 
                print("\tEnrolling in Subject-" + new_subject.subject_id)
                print("\tYou are now enrolled in", len(student_record["subjects"]), "out of 4 subjects.")
                total_marks = 0
                for subject in student_record["subjects"]:
                    total_marks = total_marks + subject["mark"]
                average_mark = total_marks / len(student_record["subjects"])
                student_record["average_mark"] = average_mark
        elif choice == "r":
            subject_id = input("\tRemove Subject by ID: ") 
            found = False
            for subject in student_record["subjects"]:
                if subject["subject_id"] == subject_id:
                    student_record["subjects"].remove(subject)
                    print("\tSubject with ID", subject_id, "has been removed.")
                    print("\tYou are now enrolled in", len(student_record["subjects"]), "out of 4 subjects.")
                    found = True
                    if len(student_record["subjects"]) > 0:
                        total_marks = 0
                        for subject in student_record["subjects"]:
                            total_marks = total_marks + subject["mark"]
                        average_mark = total_marks / len(student_record["subjects"])
                        student_record["average_mark"] = average_mark
                    else:
                        student_record["average_mark"] = 0
                    break
            if found == False:
                print("\tSubject with ID", subject_id, "not found.")
                
        elif choice == "s":
            print("\tShowing", len(student_record["subjects"]), "subjects.")   
            for subject in student_record["subjects"]:
                print("\t[ Subject::" + str(subject["subject_id"]) + " -- mark =", subject["mark"], "-- grade =", subject["grade"], "]") 
        elif choice == "x":
            print("\tExiting Subject Enrolment System")
            return
        else:
            print("\tInvalid choice")