import json

class Employee:
    def __init__(self, name, ID, title, department):
        self.name = name
        self.ID = ID
        self.title = title
        self.department = department
        
    def employee_detail(self):
        print(f"Name : {self.name}, ID : {self.ID}, Title : {self.title}, Department : {self.department}")
        
    def __str__(self):
        return f"Name: {self.name}, ID: {self.ID}"
    
    
class Department:
    def __init__(self, name):
        self.name = name
        self.employes = []
        
    def add_employee(self, employee):
        for emp in self.employes:
            if emp.ID == employee.ID:
                print("Employee already exist")
        self.employes.append(employee)
        print("{employee} added in the department")
        
    def remove_employee(self, ID):
        for i in self.employes:
            if i.ID == ID:
                self.employes.remove(i)
                print("{ID} employee successfully removed")
        print("{ID} not found in the department")
                
    def employees_list(self):
        if not self.employes :
            print("No employees record found in the list")
        else:
            for emp in self.employes:
                print(emp)
                
class Company:
    def __init__(self):
        self.departments = {}
    
    def add_department(self, department):
        if department not in self.departments:
            self.departments[department] = Department(department)
            print(f"{department} added successfully")
        else:
            print(f"{department} already exists")

    def display_menu(self):
        print("Employee Management System Menu:")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Display Department")
        print("4. Add Department")
        print("5. Exit")        
    def run_system(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.remove_employee()
            elif choice == '3':
                self.list_employees()
            elif choice == '4':
                self.add_departments()
            elif choice == '5':
                print("exit")
                break
            else:
                print("Invalid choice.Please enter choice between 1 to 4.")
                
    def add_employee(self):
        department = input("Enter department name: ")
        if department in self.departments:
            name = input("Enter employee name: ")
            ID = input("Enter employee ID: ")
            title = input("Enter employee title: ")
            employee = Employee(name, ID, title, department)
            self.departments[department].add_employee(employee)
            print("Employee {name} added successfully")
        else:
            print("{department} does not exist. Please add the department first.")

    def remove_employee(self):
        department = input("Enter department name: ")
        if department in self.departments:
            dep = self.departments[department]
            ID = input("Enter employee ID to remove: ")
            dep.remove_employee(ID)
        else:
            print("{department} does not exist.")
            
    def list_employees(self):
        department = input("Enter department name: ")
        if department in self.departments:
            dep = self.departments[department]
            print(f"Employees in department {department}:")
            for employee in dep.employes:
                print(employee)
        else:
            print("Department does not exist.")
    def add_departments(self):
        department = input("Enter new department name: ")
        self.add_department(department)
     
    # optional portion start from here       
    def save_data(self, filename):
        with open(filename, 'w') as file:
            department_data = []
            for department in self.departments.values():
                department_data.append(department.__dict__)
            json.dump(department_data, file)

    def load_data(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            for dep in data:
                department = Department(dep['name'])
                department.employees = [Employee(emp['name'], emp['emp_id'], emp['title'], emp['department']) for emp in dep['employes']]
                for emp in dep['employes']:
                    department.employes = Employee(emp['name'], emp['ID'], emp['title'], emp['department'])
                self.departments[department.name] = department
                
# Making object of COmpany class         
company = Company()
# Execute this portion if you want to perform some choice based opertion on this code.
company.run_system()


#optional portion
# to save the data in file
file_name = input("Enter the File name: ")
company.save_data(file_name)

#to load the data from json file
file_name = input("Enter : ") # Enter either file name if exist in same folder else enter the file path
company.load_data(file_name)

