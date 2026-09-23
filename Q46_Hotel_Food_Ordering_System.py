# 46. Hotel Food Ordering System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Order:
    def __init__(self, customer_name, food_item, order_amount):
        self.customer_name = customer_name
        self.food_item = food_item
        self.order_amount = order_amount

    def display(self):
        print(self)

    def __str__(self):
        return f"{self.customer_name} | {self.food_item} | {self.order_amount}"


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
    customer_name = parts[0]
    food_item = parts[1]
    order_amount = int(parts[2])
    obj.add(Order(customer_name, food_item, order_amount))

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
