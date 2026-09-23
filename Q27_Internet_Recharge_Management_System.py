# 27. Internet Recharge Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Recharge:
    def __init__(self, customer_name, mobile_number, recharge_amount):
        self.customer_name = customer_name
        self.mobile_number = mobile_number
        self.recharge_amount = recharge_amount

    def category(self):
        # PDF gives plan names but no amount thresholds; practice assumption.
        if self.recharge_amount >= 10000:
            return "Annual"
        elif self.recharge_amount >= 1000:
            return "Monthly"
        return "Daily"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.customer_name} | {self.mobile_number} | {self.recharge_amount} | {self.category()}"


class ServiceProvider:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = ServiceProvider()

for _ in range(n):
    parts = input().split(",")
    customer_name = parts[0]
    mobile_number = parts[1]
    recharge_amount = int(parts[2])
    obj.add(Recharge(customer_name, mobile_number, recharge_amount))

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
