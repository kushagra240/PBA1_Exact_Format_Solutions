# 41. Laptop Repair Service Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Laptop:
    def __init__(self, customer_name, laptop_brand, repair_cost):
        self.customer_name = customer_name
        self.laptop_brand = laptop_brand
        self.repair_cost = repair_cost

    def category(self):
        # PDF gives names but no thresholds; practice assumption.
        if self.repair_cost >= 10000:
            return "Major"
        elif self.repair_cost >= 5000:
            return "Moderate"
        return "Minor"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.customer_name} | {self.laptop_brand} | {self.repair_cost} | {self.category()}"


class ServiceCenter:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = ServiceCenter()

for _ in range(n):
    parts = input().split(",")
    customer_name = parts[0]
    laptop_brand = parts[1]
    repair_cost = int(parts[2])
    obj.add(Laptop(customer_name, laptop_brand, repair_cost))

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
