# 45. Pharmacy Billing Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Bill:
    def __init__(self, customer_name, bill_number, bill_amount):
        self.customer_name = customer_name
        self.bill_number = bill_number
        self.bill_amount = bill_amount

    def category(self):
        # PDF gives names but no bill thresholds; practice assumption.
        if self.bill_amount >= 10000:
            return "High Value"
        elif self.bill_amount >= 5000:
            return "Medium Value"
        return "Low Value"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.customer_name} | {self.bill_number} | {self.bill_amount} | {self.category()}"


class Pharmacy:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = Pharmacy()

for _ in range(n):
    parts = input().split(",")
    customer_name = parts[0]
    bill_number = parts[1]
    bill_amount = int(parts[2])
    obj.add(Bill(customer_name, bill_number, bill_amount))

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
