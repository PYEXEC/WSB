class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def display(self):
        print(f"Student ID: {self.student_id}\n"
              f"Student name: {self.student_name}")


student = Student(634, "Jan Kowalski")
setattr(student, "student_class", "VII")
student.display()
print(student.student_class)
