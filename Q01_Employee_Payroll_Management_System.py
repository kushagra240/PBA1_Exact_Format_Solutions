# 1. Employee Payroll Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Employee:
    def __init__(self, employee_name, employee_id, basic_salary):
        self.employee_name = employee_name
        self.employee_id = employee_id
        self.basic_salary = basic_salary

    def category(self):
        if self.basic_salary >= 80000:
            return "Grade A"
        elif self.basic_salary >= 60000:
            return "Grade B"
        elif self.basic_salary >= 40000:
            return "Grade C"
        return "Grade D"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.employee_name} | {self.employee_id} | {self.basic_salary} | {self.category()}"


class Company:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = Company()

for _ in range(n):
    parts = input().split(",")
    employee_name = parts[0]
    employee_id = parts[1]
    basic_salary = int(parts[2])
    obj.add(Employee(employee_name, employee_id, basic_salary))

obj.display_all()

# ============================================================
# CO2 - Dynamic Programming
# ============================================================

# CO2 - Dynamic Programming: Fibonacci using Memoization (Top-Down)
n = int(input())
memo = {0: 0, 1: 1}

def fib(x):
    if x not in memo:
        memo[x] = fib(x - 1) + fib(x - 2)
    return memo[x]

print(*[fib(i) for i in range(n)])
