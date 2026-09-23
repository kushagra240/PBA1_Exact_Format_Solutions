# 44. Petrol Pump Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Customer:
    def __init__(self, customer_name, fuel_type, amount_paid):
        self.customer_name = customer_name
        self.fuel_type = fuel_type
        self.amount_paid = amount_paid

    def display(self):
        print(self)

    def __str__(self):
        return f"{self.customer_name} | {self.fuel_type} | {self.amount_paid}"


class PetrolPump:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = PetrolPump()

for _ in range(n):
    parts = input().split(",")
    customer_name = parts[0]
    fuel_type = parts[1]
    amount_paid = int(parts[2])
    obj.add(Customer(customer_name, fuel_type, amount_paid))

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
