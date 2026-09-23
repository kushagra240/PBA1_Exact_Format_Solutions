# 43. Examination Hall Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Student:
    def __init__(self, student_name, roll_number, hall_number):
        self.student_name = student_name
        self.roll_number = roll_number
        self.hall_number = hall_number

    def category(self):
        # PDF gives blocks but no hall-number mapping; practice assumption.
        if self.hall_number <= 100:
            return "Block A"
        elif self.hall_number <= 200:
            return "Block B"
        return "Block C"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.student_name} | {self.roll_number} | {self.hall_number} | {self.category()}"


class ExamHall:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = ExamHall()

for _ in range(n):
    parts = input().split(",")
    student_name = parts[0]
    roll_number = int(parts[1])
    hall_number = int(parts[2])
    obj.add(Student(student_name, roll_number, hall_number))

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
