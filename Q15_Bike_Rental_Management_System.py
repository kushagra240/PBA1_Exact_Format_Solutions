# 15. Bike Rental Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Bike:
    def __init__(self, bike_number, model, rent_per_day):
        self.bike_number = bike_number
        self.model = model
        self.rent_per_day = rent_per_day

    def category(self):
        # PDF gives names but no thresholds; practice assumption.
        if self.rent_per_day >= 2000:
            return "Premium"
        elif self.rent_per_day >= 1000:
            return "Standard"
        return "Economy"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.bike_number} | {self.model} | {self.rent_per_day} | {self.category()}"


class RentalAgency:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = RentalAgency()

for _ in range(n):
    parts = input().split(",")
    bike_number = parts[0]
    model = parts[1]
    rent_per_day = int(parts[2])
    obj.add(Bike(bike_number, model, rent_per_day))

obj.display_all()

# ============================================================
# CO2 - Dynamic Programming
# ============================================================

# CO2 - Dynamic Programming: Rod Cutting
# Input: N / N prices for lengths 1..N
n = int(input())
prices = list(map(int, input().split()))
dp = [0] * (n + 1)
for length in range(1, n + 1):
    for cut in range(1, length + 1):
        dp[length] = max(dp[length], prices[cut - 1] + dp[length - cut])
print(dp[n])
