class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary
        
        self.hra = 0
        self.da = 0
        self.tax = 0
        self.gross_salary = 0
        self.net_salary = 0

    def calculate_salary(self):
        self.hra = 0.20 * self.basic_salary   # 20% HRA
        self.da = 0.10 * self.basic_salary    # 10% DA
        self.tax = 0.05 * self.basic_salary   # 5% Tax

        self.gross_salary = self.basic_salary + self.hra + self.da
        self.net_salary = self.gross_salary - self.tax

    def display(self):
        print("\n----- Employee Salary Report -----")
        print("Employee ID      :", self.emp_id)
        print("Employee Name    :", self.name)
        print("Basic Salary     :", self.basic_salary)
        print("HRA              :", self.hra)
        print("DA               :", self.da)
        print("Tax Deduction    :", self.tax)
        print("Gross Salary     :", self.gross_salary)
        print("Net Salary       :", self.net_salary)

emp_id = int(input("Enter Employee ID: "))
name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))

emp = Employee(emp_id, name, basic_salary)

emp.calculate_salary()
emp.display()