# 39. Apartment Maintenance Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Resident:
    def __init__(self, resident_name, flat_number, maintenance_fee):
        self.resident_name = resident_name
        self.flat_number = flat_number
        self.maintenance_fee = maintenance_fee

    def category(self):
        return "Paid" if self.amount >= 1 else "Pending"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.resident_name} | {self.flat_number} | {self.maintenance_fee} | {self.category()}"


class Society:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = Society()

for _ in range(n):
    parts = input().split(",")
    resident_name = parts[0]
    flat_number = parts[1]
    maintenance_fee = int(parts[2])
    obj.add(Resident(resident_name, flat_number, maintenance_fee))

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
