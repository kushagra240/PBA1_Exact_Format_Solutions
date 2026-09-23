# 28. Digital Wallet Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class User:
    def __init__(self, user_name, wallet_id, wallet_balance):
        self.user_name = user_name
        self.wallet_id = wallet_id
        self.wallet_balance = wallet_balance

    def category(self):
        # PDF gives names but no balance thresholds; practice assumption.
        if self.wallet_balance >= 10000:
            return "Gold"
        elif self.wallet_balance >= 5000:
            return "Silver"
        return "Bronze"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.user_name} | {self.wallet_id} | {self.wallet_balance} | {self.category()}"


class Wallet:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = Wallet()

for _ in range(n):
    parts = input().split(",")
    user_name = parts[0]
    wallet_id = parts[1]
    wallet_balance = int(parts[2])
    obj.add(User(user_name, wallet_id, wallet_balance))

obj.display_all()

# ============================================================
# CO2 - Dynamic Programming
# ============================================================

# CO2 - Dynamic Programming: House Robber
# Input: N / N house values
n = int(input())
values = list(map(int, input().split()))
prev2 = 0
prev1 = 0
for value in values:
    current = max(prev1, prev2 + value)
    prev2 = prev1
    prev1 = current
print(prev1)
