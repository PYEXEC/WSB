class Student:
    student_name = "Jan Kowalski"
    marks = 78


print(f"Student name: {getattr(Student, 'student_name')}")
print(f"Marks: {getattr(Student, 'marks')}")
setattr(Student, "student_name", "Janina Kowalska")
setattr(Student, "marks", 87)
print(f"Student name: {getattr(Student, 'student_name')}")
print(f"Marks: {getattr(Student, 'marks')}")
