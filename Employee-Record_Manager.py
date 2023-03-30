class Employee:
    def __init__(self, name, employee_id, job_title, salary):
        self.name = name
        self.employee_id = employee_id
        self.job_title = job_title
        self.salary = salary

    def __str__(self):
        return f"{self.name} (ID: {self.employee_id}, Job Title: {self.job_title}, Salary: {self.salary})"


class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee_id):
        employee = self.find_employee_by_id(employee_id)
        if employee is not None:
            self.employees.remove(employee)

    def find_employee_by_id(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        return None

    def view_employees(self):
        for employee in self.employees:
            print(employee)


def main():
    employee_manager = EmployeeManager()

    while True:
        print("\nEmployee Record Manager")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. View Employees")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter employee name: ")
            employee_id = input("Enter employee ID: ")
            job_title = input("Enter job title: ")
            salary = float(input("Enter salary: "))
            employee = Employee(name, employee_id, job_title, salary)
            employee_manager.add_employee(employee)
        elif choice == 2:
            employee_id = input("Enter employee ID: ")
            employee_manager.remove_employee(employee_id)
        elif choice == 3:
            employee_manager.view_employees()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
