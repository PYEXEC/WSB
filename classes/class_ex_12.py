class Student:
    school = 'Forward Thinking'
    address = '2626/Z Overlook Drive, COLUMBUS'


student_1 = Student()
student_2 = Student()
student_1.student_id = 1931
student_1.student_name = "Jan Kowalski"
student_2.student_id = 1292
student_2.marks_language = 34
student_2.marks_science = 39
student_2.marks_math = 99
students = [student_1, student_2]
for student in students:
    print('\n')
    for attr in student.__dict__:
        print(f'{attr} -> {getattr(student, attr)}')
