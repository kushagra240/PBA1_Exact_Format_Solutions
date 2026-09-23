# 36. Clothing Store Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Cloth:
    def __init__(self, brand_name, size, price):
        self.brand_name = brand_name
        self.size = size
        self.price = price

    def category(self):
        # PDF gives names but no price thresholds; practice assumption.
        if self.price >= 5000:
            return "Premium"
        elif self.price >= 2000:
            return "Standard"
        return "Budget"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.brand_name} | {self.size} | {self.price} | {self.category()}"


class Store:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = Store()

for _ in range(n):
    parts = input().split(",")
    brand_name = parts[0]
    size = parts[1]
    price = int(parts[2])
    obj.add(Cloth(brand_name, size, price))

obj.display_all()

# ============================================================
# CO2 - Dynamic Programming
# ============================================================

# CO2 - Dynamic Programming: House Robber
# Input: N / N house values
n = int(input())
values = list(map(int, input().split()))
prev2 = 0
prev1 = 0
for value in values:
    current = max(prev1, prev2 + value)
    prev2 = prev1
    prev1 = current
print(prev1)
