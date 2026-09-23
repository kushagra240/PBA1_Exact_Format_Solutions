# 12. Bakery Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class BakeryItem:
    def __init__(self, item_name, category, price):
        self.item_name = item_name
        self.category = category
        self.price = price

    def display(self):
        print(self)

    def __str__(self):
        return f"{self.item_name} | {self.category} | {self.price}"


class Bakery:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = Bakery()

for _ in range(n):
    parts = input().split(",")
    item_name = parts[0]
    category = parts[1]
    price = int(parts[2])
    obj.add(BakeryItem(item_name, category, price))

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
