# 22. Railway Ticket Booking Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Passenger:
    def __init__(self, passenger_name, train_number, ticket_fare):
        self.passenger_name = passenger_name
        self.train_number = train_number
        self.ticket_fare = ticket_fare

    def category(self):
        # PDF gives class names but no fare thresholds; practice assumption.
        if self.ticket_fare >= 3000:
            return "First Class"
        elif self.ticket_fare >= 1500:
            return "Second Class"
        return "Sleeper Class"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.passenger_name} | {self.train_number} | {self.ticket_fare} | {self.category()}"


class Railway:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = Railway()

for _ in range(n):
    parts = input().split(",")
    passenger_name = parts[0]
    train_number = parts[1]
    ticket_fare = int(parts[2])
    obj.add(Passenger(passenger_name, train_number, ticket_fare))

obj.display_all()

# ============================================================
# CO2 - Dynamic Programming
# ============================================================

# CO2 - Dynamic Programming: Coin Change - Number of Ways
# Input: C / coin values / amount
c = int(input())
coins = list(map(int, input().split()))
amount = int(input())
dp = [0] * (amount + 1)
dp[0] = 1
for coin in coins:
    for x in range(coin, amount + 1):
        dp[x] += dp[x - coin]
print(dp[amount])
