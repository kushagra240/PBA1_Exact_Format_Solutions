# 8. Hospital Patient Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Patient:
    def __init__(self, name, patient_id, treatment_cost):
        self.name = name
        self.patient_id = patient_id
        self.treatment_cost = treatment_cost

    def category(self):
        # PDF gives names but no thresholds; practice assumption.
        if self.treatment_cost >= 50000:
            return "High Expense"
        elif self.treatment_cost >= 20000:
            return "Medium Expense"
        return "Low Expense"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.name} | {self.patient_id} | {self.treatment_cost} | {self.category()}"


class Hospital:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = Hospital()

for _ in range(n):
    parts = input().split(",")
    name = parts[0]
    patient_id = parts[1]
    treatment_cost = int(parts[2])
    obj.add(Patient(name, patient_id, treatment_cost))

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
