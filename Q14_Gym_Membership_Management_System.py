# 14. Gym Membership Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Member:
    def __init__(self, member_name, membership_type, annual_fee):
        self.member_name = member_name
        self.membership_type = membership_type
        self.annual_fee = annual_fee

    def category(self):
        # PDF gives names but no thresholds; practice assumption.
        if self.annual_fee >= 20000:
            return "Gold"
        elif self.annual_fee >= 10000:
            return "Silver"
        return "Bronze"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.member_name} | {self.membership_type} | {self.annual_fee} | {self.category()}"


class Gym:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = Gym()

for _ in range(n):
    parts = input().split(",")
    member_name = parts[0]
    membership_type = parts[1]
    annual_fee = int(parts[2])
    obj.add(Member(member_name, membership_type, annual_fee))

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
