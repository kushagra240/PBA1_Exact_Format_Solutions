# 33. Passport Application Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Applicant:
    def __init__(self, applicant_name, passport_id, application_fee):
        self.applicant_name = applicant_name
        self.passport_id = passport_id
        self.application_fee = application_fee

    def category(self):
        # PDF gives names but no fee threshold; practice assumption.
        return "Tatkal" if self.application_fee >= 3500 else "Normal"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.applicant_name} | {self.passport_id} | {self.application_fee} | {self.category()}"


class PassportOffice:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = PassportOffice()

for _ in range(n):
    parts = input().split(",")
    applicant_name = parts[0]
    passport_id = parts[1]
    application_fee = int(parts[2])
    obj.add(Applicant(applicant_name, passport_id, application_fee))

obj.display_all()

# ============================================================
# CO2 - Dynamic Programming
# ============================================================

# CO2 - Dynamic Programming: Unique Paths
m, n = map(int, input().split())
dp = [1] * n
for i in range(1, m):
    for j in range(1, n):
        dp[j] += dp[j - 1]
print(dp[n - 1])
