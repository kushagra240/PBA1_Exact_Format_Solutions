# 16. Blood Bank Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Donor:
    def __init__(self, donor_name, blood_group, age):
        self.donor_name = donor_name
        self.blood_group = blood_group
        self.age = age

    def display(self):
        print(self)

    def __str__(self):
        return f"{self.donor_name} | {self.blood_group} | {self.age}"


class BloodBank:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = BloodBank()

for _ in range(n):
    parts = input().split(",")
    donor_name = parts[0]
    blood_group = parts[1]
    age = int(parts[2])
    obj.add(Donor(donor_name, blood_group, age))

obj.display_all()

# ============================================================
# CO2 - Dynamic Programming
# ============================================================

# CO2 - Dynamic Programming: Longest Common Subsequence
a = input()
b = input()
dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[len(a)][len(b)])
