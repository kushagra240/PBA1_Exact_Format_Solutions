# 25. Electricity Bill Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Consumer:
    def __init__(self, consumer_name, consumer_number, electricity_bill_amount):
        self.consumer_name = consumer_name
        self.consumer_number = consumer_number
        self.electricity_bill_amount = electricity_bill_amount

    def category(self):
        # PDF gives names but no thresholds; practice assumption.
        if self.electricity_bill_amount >= 5000:
            return "High Consumption"
        elif self.electricity_bill_amount >= 2500:
            return "Medium Consumption"
        return "Low Consumption"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.consumer_name} | {self.consumer_number} | {self.electricity_bill_amount} | {self.category()}"


class ElectricityBoard:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = ElectricityBoard()

for _ in range(n):
    parts = input().split(",")
    consumer_name = parts[0]
    consumer_number = parts[1]
    electricity_bill_amount = int(parts[2])
    obj.add(Consumer(consumer_name, consumer_number, electricity_bill_amount))

obj.display_all()

# ============================================================
# CO2 - Dynamic Programming
# ============================================================

# CO2 - Dynamic Programming: Minimum Cost Path
# Input: rows cols / matrix rows
rows, cols = map(int, input().split())
cost = [list(map(int, input().split())) for _ in range(rows)]
for i in range(1, rows):
    cost[i][0] += cost[i - 1][0]
for j in range(1, cols):
    cost[0][j] += cost[0][j - 1]
for i in range(1, rows):
    for j in range(1, cols):
        cost[i][j] += min(cost[i - 1][j], cost[i][j - 1])
print(cost[rows - 1][cols - 1])
