# 26. Water Supply Billing Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Consumer:
    def __init__(self, consumer_name, consumer_id, water_bill_amount):
        self.consumer_name = consumer_name
        self.consumer_id = consumer_id
        self.water_bill_amount = water_bill_amount

    def category(self):
        # PDF gives names but no thresholds; practice assumption.
        if self.water_bill_amount >= 5000:
            return "High Usage"
        elif self.water_bill_amount >= 2500:
            return "Moderate Usage"
        return "Low Usage"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.consumer_name} | {self.consumer_id} | {self.water_bill_amount} | {self.category()}"


class WaterBoard:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = WaterBoard()

for _ in range(n):
    parts = input().split(",")
    consumer_name = parts[0]
    consumer_id = parts[1]
    water_bill_amount = int(parts[2])
    obj.add(Consumer(consumer_name, consumer_id, water_bill_amount))

obj.display_all()

# ============================================================
# CO2 - Dynamic Programming
# ============================================================

# CO2 - Dynamic Programming: Fibonacci using Memoization (Top-Down)
n = int(input())
memo = {0: 0, 1: 1}

def fib(x):
    if x not in memo:
        memo[x] = fib(x - 1) + fib(x - 2)
    return memo[x]

print(*[fib(i) for i in range(n)])
