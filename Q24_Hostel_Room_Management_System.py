# 24. Hostel Room Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Student:
    def __init__(self, student_name, room_number, hostel_fee):
        self.student_name = student_name
        self.room_number = room_number
        self.hostel_fee = hostel_fee

    def category(self):
        # PDF gives room categories but no rule; practice assumption.
        if self.hostel_fee >= 60000:
            return "Single"
        elif self.hostel_fee >= 40000:
            return "Double"
        return "Triple Sharing"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.student_name} | {self.room_number} | {self.hostel_fee} | {self.category()}"


class Hostel:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = Hostel()

for _ in range(n):
    parts = input().split(",")
    student_name = parts[0]
    room_number = parts[1]
    hostel_fee = int(parts[2])
    obj.add(Student(student_name, room_number, hostel_fee))

obj.display_all()

# ============================================================
# CO2 - Dynamic Programming
# ============================================================

# CO2 - Dynamic Programming: Climbing Stairs
n = int(input())
if n <= 1:
    print(1)
else:
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    print(b)
