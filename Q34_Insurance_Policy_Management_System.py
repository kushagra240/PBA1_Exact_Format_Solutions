# 34. Insurance Policy Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Policy:
    def __init__(self, policy_number, customer_name, premium_amount):
        self.policy_number = policy_number
        self.customer_name = customer_name
        self.premium_amount = premium_amount

    def category(self):
        # PDF gives names but no premium thresholds; practice assumption.
        if self.premium_amount >= 50000:
            return "Gold"
        elif self.premium_amount >= 25000:
            return "Silver"
        return "Bronze"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.policy_number} | {self.customer_name} | {self.premium_amount} | {self.category()}"


class InsuranceCompany:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = InsuranceCompany()

for _ in range(n):
    parts = input().split(",")
    policy_number = parts[0]
    customer_name = parts[1]
    premium_amount = int(parts[2])
    obj.add(Policy(policy_number, customer_name, premium_amount))

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
