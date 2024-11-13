class Employee:
    def __init__(self, emp_id, name, department, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.position = position
        self.salary = salary

    def display_info(self):
        print(f"ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary}")

    def update_info(self, name=None, department=None, position=None, salary=None):
        if name:
            self.name = name
        if department:
            self.department = department
        if position:
            self.position = position
        if salary:
            self.salary = salary
        print("Employee information updated successfully.")

class ERPSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp_id, name, department, position, salary):
        if emp_id in self.employees:
            print("Employee with this ID already exists.")
        else:
            employee = Employee(emp_id, name, department, position, salary)
            self.employees[emp_id] = employee
            print("Employee added successfully.")

    def view_employee(self, emp_id):
        if emp_id in self.employees:
            self.employees[emp_id].display_info()
        else:
            print("Employee not found.")

    def update_employee(self, emp_id, name=None, department=None, position=None, salary=None):
        if emp_id in self.employees:
            self.employees[emp_id].update_info(name, department, position, salary)
        else:
            print("Employee not found.")

    def delete_employee(self, emp_id):
        if emp_id in self.employees:
            del self.employees[emp_id]
            print("Employee deleted successfully.")
        else:
            print("Employee not found.")

# Example Usage
erp = ERPSystem()
erp.add_employee(1, "mohamed", "HR", "Manager", 70000)
erp.add_employee(2, "ahmed", "IT", "Developer", 60000)

print("\n--- View Employee ---")
erp.view_employee(1)

print("\n--- Update Employee ---")
erp.update_employee(1, position="Senior Manager", salary=80000)
erp.view_employee(1)

print("\n--- Delete Employee ---")
erp.delete_employee(2)
erp.view_employee(2)

