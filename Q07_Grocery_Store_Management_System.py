# 7. Grocery Store Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Item:
    def __init__(self, item_name, quantity, price):
        self.item_name = item_name
        self.quantity = quantity
        self.price = price

    def display(self):
        print(self)

    def __str__(self):
        return f"{self.item_name} | {self.quantity} | {self.price}"


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
    item_name = parts[0]
    quantity = int(parts[1])
    price = int(parts[2])
    obj.add(Item(item_name, quantity, price))

obj.display_all()

# ============================================================
# CO2 - Dynamic Programming
# ============================================================

# CO2 - Dynamic Programming: 0/1 Knapsack
# Input: N / weights / values / capacity
n = int(input())
weights = list(map(int, input().split()))
values = list(map(int, input().split()))
capacity = int(input())
dp = [0] * (capacity + 1)
for i in range(n):
    for w in range(capacity, weights[i] - 1, -1):
        dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
print(dp[capacity])
