class Person:
    def __init__(self, id, name, contact_info):
        self.id = id
        self.name = name
        self.contact_info = contact_info

    def display_info(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Contact Info: {self.contact_info}")

    def update_info(self, name=None, contact_info=None):
        if name:
            self.name = name
        if contact_info:
            self.contact_info = contact_info
        print("Information updated successfully.")

class Employee(Person):
    def __init__(self, id, name, contact_info, department, position, salary):
        super().__init__(id, name, contact_info)
        self.department = department
        self.position = position
        self.salary = salary

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary}")

    def update_info(self, department=None, position=None, salary=None,):
        super().update_info()
        if department:
            self.department = department
        if position:
            self.position = position
        if salary:
            self.salary = salary

class Client(Person):
    def __init__(self, id, name, contact_info, company, industry):
        super().__init__(id, name, contact_info)
        self.company = company
        self.industry = industry

    def display_info(self):
        super().display_info()
        print(f"Company: {self.company}")
        print(f"Industry: {self.industry}")

    def update_info(self, company=None, industry=None, **kwargs):
        super().update_info(**kwargs)
        if company:
            self.company = company
        if industry:
            self.industry = industry

class ERPSystem:
    def __init__(self):
        self.employees = {}
        self.clients = {}

    def add_employee(self, id, name, contact_info, department, position, salary):
        if id in self.employees:
            print("Employee with this ID already exists.")
        else:
            employee = Employee(id, name, contact_info, department, position, salary)
            self.employees[id] = employee
            print("Employee added successfully.")

    def add_client(self, id, name, contact_info, company, industry):
        if id in self.clients:
            print("Client with this ID already exists.")
        else:
            client = Client(id, name, contact_info, company, industry)
            self.clients[id] = client
            print("Client added successfully.")

    def view_person(self, id, person_type):
        if person_type == 'employee' and id in self.employees:
            self.employees[id].display_info()
        elif person_type == 'client' and id in self.clients:
            self.clients[id].display_info()
        else:
            print(f"{person_type.capitalize()} not found.")

    def update_person(self, id, person_type, **kwargs):
        if person_type == 'employee' and id in self.employees:
            self.employees[id].update_info(**kwargs)
        elif person_type == 'client' and id in self.clients:
            self.clients[id].update_info(**kwargs)
        else:
            print(f"{person_type.capitalize()} not found.")

    def delete_person(self, id, person_type):
        if person_type == 'employee' and id in self.employees:
            del self.employees[id]
            print("Employee deleted successfully.")
        elif person_type == 'client' and id in self.clients:
            del self.clients[id]
            print("Client deleted successfully.")
        else:
            print(f"{person_type.capitalize()} not found.")

# Example Usage
erp = ERPSystem()
erp.add_employee(1, "ahmed", "ahmede@gmail.com", "devoloper", "Manager", 70000)
erp.add_client(100, "saeed", "saeed@gmail.com", "TechCorp", "Technology")

print("\n--- View Employee ---")
erp.view_person(1, "employee")

print("\n--- View Client ---")
erp.view_person(100, "client")

print("\n--- Update Employee ---")
erp.update_person(1, "employee", position="Senior Manager", salary=80000)
erp.view_person(1, "employee")

print("\n--- Delete Client ---")
erp.delete_person(100, "client")
erp.view_person(100, "client")

