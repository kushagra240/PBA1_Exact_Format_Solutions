# 17. School Fee Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Student:
    def __init__(self, name, roll_number, fee_paid):
        self.name = name
        self.roll_number = roll_number
        self.fee_paid = fee_paid

    def category(self):
        return "Paid" if self.amount >= 1 else "Pending"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.name} | {self.roll_number} | {self.fee_paid} | {self.category()}"


class School:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = School()

for _ in range(n):
    parts = input().split(",")
    name = parts[0]
    roll_number = parts[1]
    fee_paid = int(parts[2])
    obj.add(Student(name, roll_number, fee_paid))

obj.display_all()

# ============================================================
# CO2 - Dynamic Programming
# ============================================================

# CO2 - Dynamic Programming: Unique Paths
m, n = map(int, input().split())
dp = [1] * n
for i in range(1, m):
    for j in range(1, n):
        dp[j] += dp[j - 1]
print(dp[n - 1])
