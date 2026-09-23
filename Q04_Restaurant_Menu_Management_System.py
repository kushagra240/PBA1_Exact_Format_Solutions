# 4. Restaurant Menu Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class FoodItem:
    def __init__(self, item_name, price, category):
        self.item_name = item_name
        self.price = price
        self.category = category

    def display(self):
        print(self)

    def __str__(self):
        return f"{self.item_name} | {self.price} | {self.category}"


class Restaurant:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = Restaurant()

for _ in range(n):
    parts = input().split(",")
    item_name = parts[0]
    price = int(parts[1])
    category = parts[2]
    obj.add(FoodItem(item_name, price, category))

obj.display_all()

# ============================================================
# CO2 - Dynamic Programming
# ============================================================

# CO2 - Dynamic Programming: Rod Cutting
# Input: N / N prices for lengths 1..N
n = int(input())
prices = list(map(int, input().split()))
dp = [0] * (n + 1)
for length in range(1, n + 1):
    for cut in range(1, length + 1):
        dp[length] = max(dp[length], prices[cut - 1] + dp[length - cut])
print(dp[n])
