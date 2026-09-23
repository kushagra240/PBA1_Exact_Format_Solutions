# 48. Vehicle Insurance Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Vehicle:
    def __init__(self, vehicle_number, owner_name, insurance_premium):
        self.vehicle_number = vehicle_number
        self.owner_name = owner_name
        self.insurance_premium = insurance_premium

    def display(self):
        print(self)

    def __str__(self):
        return f"{self.vehicle_number} | {self.owner_name} | {self.insurance_premium}"


class InsuranceOffice:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = InsuranceOffice()

for _ in range(n):
    parts = input().split(",")
    vehicle_number = parts[0]
    owner_name = parts[1]
    insurance_premium = int(parts[2])
    obj.add(Vehicle(vehicle_number, owner_name, insurance_premium))

obj.display_all()

# ============================================================
# CO2 - Dynamic Programming
# ============================================================

# CO2 - Dynamic Programming: Edit Distance
a = input()
b = input()
prev = list(range(len(b) + 1))
for i in range(1, len(a) + 1):
    curr = [i]
    for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
            curr.append(prev[j - 1])
        else:
            curr.append(1 + min(prev[j], curr[j - 1], prev[j - 1]))
    prev = curr
print(prev[-1])
