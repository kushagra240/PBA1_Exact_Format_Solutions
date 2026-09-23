# 6. Vehicle Rental Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Vehicle:
    def __init__(self, vehicle_number, vehicle_type, rent_per_day):
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type
        self.rent_per_day = rent_per_day

    def display(self):
        print(self)

    def __str__(self):
        return f"{self.vehicle_number} | {self.vehicle_type} | {self.rent_per_day}"


class RentalAgency:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = RentalAgency()

for _ in range(n):
    parts = input().split(",")
    vehicle_number = parts[0]
    vehicle_type = parts[1]
    rent_per_day = int(parts[2])
    obj.add(Vehicle(vehicle_number, vehicle_type, rent_per_day))

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
