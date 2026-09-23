# 13. Coffee Shop Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Coffee:
    def __init__(self, coffee_name, size, price):
        self.coffee_name = coffee_name
        self.size = size
        self.price = price

    def display(self):
        print(self)

    def __str__(self):
        return f"{self.coffee_name} | {self.size} | {self.price}"


class Cafe:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = Cafe()

for _ in range(n):
    parts = input().split(",")
    coffee_name = parts[0]
    size = parts[1]
    price = int(parts[2])
    obj.add(Coffee(coffee_name, size, price))

obj.display_all()

# ============================================================
# CO2 - Dynamic Programming
# ============================================================

# CO2 - Dynamic Programming: Coin Change - Fewest Coins
# Input: C / coin values / amount
c = int(input())
coins = list(map(int, input().split()))
amount = int(input())
dp = [amount + 1] * (amount + 1)
dp[0] = 0
for x in range(1, amount + 1):
    for coin in coins:
        if coin <= x:
            dp[x] = min(dp[x], dp[x - coin] + 1)
print(-1 if dp[amount] == amount + 1 else dp[amount])
