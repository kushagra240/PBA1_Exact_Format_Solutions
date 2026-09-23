# 18. Toy Store Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Toy:
    def __init__(self, toy_name, age_group, price):
        self.toy_name = toy_name
        self.age_group = age_group
        self.price = price

    def display(self):
        print(self)

    def __str__(self):
        return f"{self.toy_name} | {self.age_group} | {self.price}"


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
    toy_name = parts[0]
    age_group = parts[1]
    price = int(parts[2])
    obj.add(Toy(toy_name, age_group, price))

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
