# 3. Student Result Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Student:
    def __init__(self, name, roll_number, marks_1, marks_2, marks_3):
        self.name = name
        self.roll_number = roll_number
        self.marks_1 = marks_1
        self.marks_2 = marks_2
        self.marks_3 = marks_3

    def average(self):
        return (self.marks_1 + self.marks_2 + self.marks_3) / 3

    def category(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        return "F"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.name} | {self.roll_number} | {self.marks_1} | {self.marks_2} | {self.marks_3} | {self.category()}"


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
    marks_1 = int(parts[2])
    marks_2 = int(parts[3])
    marks_3 = int(parts[4])
    obj.add(Student(name, roll_number, marks_1, marks_2, marks_3))

obj.display_all()

# ============================================================
# CO2 - Dynamic Programming
# ============================================================

# CO2 - Dynamic Programming: Coin Change - Fewest Coins
# Input: C / coin values / amount
c = int(input())
coins = list(map(int, input().split()))
amount = int(input())
dp = [amount + 1] * (amount + 1)
dp[0] = 0
for x in range(1, amount + 1):
    for coin in coins:
        if coin <= x:
            dp[x] = min(dp[x], dp[x - coin] + 1)
print(-1 if dp[amount] == amount + 1 else dp[amount])
