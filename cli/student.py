import json
class Student:
    def __init__(self, student_id, name, email, password):
        self.student_id = student_id #Store the supplied ID as an attribute of this student object.
        self.name = name
        self.email = email
        self.password = password
        self.subjects = []
        self.average_mark = 0
#test_student = Student("002340", "Alice", "alice@university.com", "Abcde123")
#print(test_student.student_id)
#print(test_student.subjects)
#class: The class defines the structure. An object represents one particular student.
#__init__: an initialization method that Python calls automatically for a new object.
#def __init__(self, student_id, name, email, password):定义初始化方法
    def to_dict(self):
        subject_data = []
        for subject in self.subjects:
            subject_data.append(subject.to_dict())
        return {
            "student_id": self.student_id,
            "name": self.name, 
            "email": self.email,
            "password": self.password,
            "subjects": subject_data,
            "average_mark": self.average_mark
        }
