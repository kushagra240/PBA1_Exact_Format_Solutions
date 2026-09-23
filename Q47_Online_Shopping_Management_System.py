# 47. Online Shopping Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Product:
    def __init__(self, product_name, product_id, price):
        self.product_name = product_name
        self.product_id = product_id
        self.price = price

    def category(self):
        # PDF gives names but no price thresholds; practice assumption.
        if self.price >= 10000:
            return "Premium"
        elif self.price >= 5000:
            return "Standard"
        return "Budget"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.product_name} | {self.product_id} | {self.price} | {self.category()}"


class ShoppingCart:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = ShoppingCart()

for _ in range(n):
    parts = input().split(",")
    product_name = parts[0]
    product_id = parts[1]
    price = int(parts[2])
    obj.add(Product(product_name, product_id, price))

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
