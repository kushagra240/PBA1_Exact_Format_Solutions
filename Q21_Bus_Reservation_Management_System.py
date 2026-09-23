# 21. Bus Reservation Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Passenger:
    def __init__(self, passenger_name, ticket_number, ticket_fare):
        self.passenger_name = passenger_name
        self.ticket_number = ticket_number
        self.ticket_fare = ticket_fare

    def category(self):
        # PDF gives names but no thresholds; practice assumption.
        if self.ticket_fare >= 5000:
            return "Premium"
        elif self.ticket_fare >= 2000:
            return "Standard"
        return "Economy"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.passenger_name} | {self.ticket_number} | {self.ticket_fare} | {self.category()}"


class Bus:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = Bus()

for _ in range(n):
    parts = input().split(",")
    passenger_name = parts[0]
    ticket_number = parts[1]
    ticket_fare = int(parts[2])
    obj.add(Passenger(passenger_name, ticket_number, ticket_fare))

obj.display_all()

# ============================================================
# CO2 - Dynamic Programming
# ============================================================

# CO2 - Dynamic Programming: Fibonacci using Tabulation (Bottom-Up)
n = int(input())
if n <= 0:
    print()
elif n == 1:
    print(0)
else:
    dp = [0] * n
    dp[1] = 1
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(*dp)
