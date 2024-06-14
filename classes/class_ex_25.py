class Employee:
    def __init__(self, emp_id: str, emp_name: str, emp_salary: (int, float), emp_department: str):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def assign_department(self, department: str):
        self.emp_department = department

    def calculate_emp_salary(self, salary, hours_worked):
        overtime = 0
        if hours_worked > 50:
            overtime = hours_worked - 50
        overtime_amount = overtime * (salary / 50)
        self.emp_salary = self.emp_salary + overtime_amount

    def print_employee_details(self):
        print(f"Employee ID: {self.emp_id}"
              f"Employee name: {self.emp_name}\n"
              f"Salary: {self.emp_salary}\n"
              f"Department: {self.emp_department}\n"
              "----------------------------------"
              )


employee_1 = Employee("E001", "Jan Kowalski", 5000, "Handlowy")
employee_2 = Employee("E049", "Krzysztof Nowak", 7500, "Techniczny")

print("Dane pracowników:\n")
employee_1.print_employee_details()
employee_2.print_employee_details()

employee_1.assign_department("Marketing")

employee_2.calculate_emp_salary(7500, 80)

print("Dane pracowników po aktualizacji:\n")
employee_1.print_employee_details()
employee_2.print_employee_details()
