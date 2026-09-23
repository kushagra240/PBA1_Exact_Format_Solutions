# 5. Mobile Store Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def category(self):
        # PDF gives names but no thresholds; practice assumption.
        if self.price >= 50000:
            return "Premium"
        elif self.price >= 20000:
            return "Mid-range"
        return "Budget"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.brand} | {self.model} | {self.price} | {self.category()}"


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
    brand = parts[0]
    model = parts[1]
    price = int(parts[2])
    obj.add(Mobile(brand, model, price))

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
