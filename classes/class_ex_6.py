def student_data(student_id, **kwargs):
    print(f"Student ID: {student_id}\n")
    if "student_name" in kwargs:
        print(f"Student name: $ {kwargs['student_name']}")

    if "student_name" and "student_class" in kwargs:
        print(f"Student name: $ {kwargs['student_name']}")
        print(f"Student class: $ {kwargs['student_class']}")


student_data(student_id=642, student_name="Jan Kowalski")
student_data(student_id=139, student_name="Janina Nowak", student_class="IV")
