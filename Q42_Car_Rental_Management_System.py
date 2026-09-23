# 42. Car Rental Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Car:
    def __init__(self, car_number, model, rent_per_day):
        self.car_number = car_number
        self.model = model
        self.rent_per_day = rent_per_day

    def category(self):
        # PDF gives names but no rent thresholds; practice assumption.
        if self.rent_per_day >= 10000:
            return "Luxury"
        elif self.rent_per_day >= 5000:
            return "Sedan"
        return "Hatchback"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.car_number} | {self.model} | {self.rent_per_day} | {self.category()}"


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
    car_number = parts[0]
    model = parts[1]
    rent_per_day = int(parts[2])
    obj.add(Car(car_number, model, rent_per_day))

obj.display_all()

# ============================================================
# CO2 - Dynamic Programming
# ============================================================

# CO2 - Dynamic Programming: 0/1 Knapsack
# Input: N / weights / values / capacity
n = int(input())
weights = list(map(int, input().split()))
values = list(map(int, input().split()))
capacity = int(input())
dp = [0] * (capacity + 1)
for i in range(n):
    for w in range(capacity, weights[i] - 1, -1):
        dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
print(dp[capacity])
