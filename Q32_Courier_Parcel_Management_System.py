# 32. Courier Parcel Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Parcel:
    def __init__(self, parcel_id, sender_name, parcel_weight):
        self.parcel_id = parcel_id
        self.sender_name = sender_name
        self.parcel_weight = parcel_weight

    def category(self):
        # PDF gives names but no weight thresholds; practice assumption.
        if self.parcel_weight >= 10:
            return "Heavy"
        elif self.parcel_weight >= 5:
            return "Medium"
        return "Light"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.parcel_id} | {self.sender_name} | {self.parcel_weight} | {self.category()}"


class CourierService:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = CourierService()

for _ in range(n):
    parts = input().split(",")
    parcel_id = parts[0]
    sender_name = parts[1]
    parcel_weight = int(parts[2])
    obj.add(Parcel(parcel_id, sender_name, parcel_weight))

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
