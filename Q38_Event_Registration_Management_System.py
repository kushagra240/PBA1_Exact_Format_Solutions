# 38. Event Registration Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Participant:
    def __init__(self, participant_name, registration_number, registration_fee):
        self.participant_name = participant_name
        self.registration_number = registration_number
        self.registration_fee = registration_fee

    def category(self):
        # PDF gives names but no fee threshold; practice assumption.
        return "VIP" if self.registration_fee >= 5000 else "Regular"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.participant_name} | {self.registration_number} | {self.registration_fee} | {self.category()}"


class Event:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = Event()

for _ in range(n):
    parts = input().split(",")
    participant_name = parts[0]
    registration_number = parts[1]
    registration_fee = int(parts[2])
    obj.add(Participant(participant_name, registration_number, registration_fee))

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
