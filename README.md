# Python_Casestudy_3

# 💼 Employee Salary Management System (Python - OOP)

## 📌 Overview

This project is a simple **Employee Salary Management System** built using **Object-Oriented Programming (OOP)** in Python.
It helps in managing employee details and automatically calculating salary components such as **HRA, DA, Tax, Gross Salary, and Net Salary**.

The system demonstrates core OOP concepts like **Class, Object, Encapsulation, and Abstraction**.

---

## 🎯 Features

* Store employee details (ID, Name, Basic Salary)
* Automatic salary calculation
* Computes:

  * HRA (House Rent Allowance)
  * DA (Dearness Allowance)
  * Tax Deduction
  * Gross Salary
  * Net Salary
* Displays a structured salary report
* Easy to extend and modify

---

## 🧮 Salary Calculation Rules

| Component    | Formula             |
| ------------ | ------------------- |
| HRA          | 20% of Basic Salary |
| DA           | 10% of Basic Salary |
| Tax          | 5% of Basic Salary  |
| Gross Salary | Basic + HRA + DA    |
| Net Salary   | Gross - Tax         |

---

## 🏗️ OOP Concepts Used

### ✔ Class & Object

* `Employee` class is used to define structure
* Object is created to handle employee data

### ✔ Encapsulation

* Employee data and salary methods are enclosed within a class

### ✔ Abstraction

* User interacts only with methods like:

  * `calculate_salary()`
  * `display()`

---

## 🧾 Code Structure

* `__init__()` → Initializes employee details
* `calculate_salary()` → Computes all salary components
* `display()` → Prints formatted salary report

---

## ▶️ How to Run

1. Make sure Python is installed
2. Save the code in a file:

   ```bash
   employee.py
   ```
3. Run the program:

   ```bash
   python3 employee.py
   ```

---

## 🖥️ Sample Output

```
Enter Employee ID: 101
Enter Employee Name: Nikhil
Enter Basic Salary: 50000

----- Employee Salary Report -----
Employee ID      : 101
Employee Name    : Nikhil
Basic Salary     : 50000.0
HRA              : 10000.0
DA               : 5000.0
Tax Deduction    : 2500.0
Gross Salary     : 65000.0
Net Salary       : 62500.0
```

---

## 🚀 Future Enhancements

* Support multiple employees
* Add bonus and additional deductions
* Store data in files or database
* Build GUI using Tkinter
* Export payslip as PDF

---

## 📚 Conclusion

This project provides a basic but scalable approach to managing employee salaries using OOP principles. It reduces manual errors and improves efficiency while keeping the system modular and easy to expand.

---

## 👨‍💻 Author

**Nikhil Yadav**
