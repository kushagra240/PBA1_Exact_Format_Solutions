# 49. Sports Equipment Store Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Equipment:
    def __init__(self, equipment_name, quantity, price):
        self.equipment_name = equipment_name
        self.quantity = quantity
        self.price = price

    def display(self):
        print(self)

    def __str__(self):
        return f"{self.equipment_name} | {self.quantity} | {self.price}"


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
    equipment_name = parts[0]
    quantity = int(parts[1])
    price = int(parts[2])
    obj.add(Equipment(equipment_name, quantity, price))

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
