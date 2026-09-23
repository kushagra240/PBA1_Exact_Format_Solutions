# 37. Plant Nursery Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Plant:
    def __init__(self, plant_name, plant_type, price):
        self.plant_name = plant_name
        self.plant_type = plant_type
        self.price = price

    def display(self):
        print(self)

    def __str__(self):
        return f"{self.plant_name} | {self.plant_type} | {self.price}"


class Nursery:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = Nursery()

for _ in range(n):
    parts = input().split(",")
    plant_name = parts[0]
    plant_type = parts[1]
    price = int(parts[2])
    obj.add(Plant(plant_name, plant_type, price))

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
