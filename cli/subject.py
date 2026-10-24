import random

class Subject:
    def __init__(self):
        self.subject_id = self.generateSubjectID()
        self.assignMarkAndGrade()

    def generateSubjectID(self):
        # Generate a random subject ID from 1 to 999
        subject_id = random.randint(1, 999)

        # Convert it to a 3 digit ID
        if subject_id < 10:
            return "00" + str(subject_id)
        elif subject_id < 100:
            return "0" + str(subject_id)
        else:
            return str(subject_id)
        
    def assignMarkAndGrade(self):
        # Generate a random mark from 25 to 100
        self.mark = random.randint(25, 100)

        if self.mark >= 85:
            self.grade = "HD"
        elif self.mark >= 75:
            self.grade = "D"
        elif self.mark >= 65:
            self.grade = "C"
        elif self.mark >= 50:
            self.grade = "P"
        else:
            self.grade = "Z"

    def to_dict(self):
        return {
            "subject_id": self.subject_id,
            "mark": self.mark,
            "grade": self.grade
        }