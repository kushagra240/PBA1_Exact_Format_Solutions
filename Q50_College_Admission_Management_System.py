# 50. College Admission Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Applicant:
    def __init__(self, applicant_name, application_id, entrance_examination_score):
        self.applicant_name = applicant_name
        self.application_id = application_id
        self.entrance_examination_score = entrance_examination_score

    def category(self):
        # PDF gives names but no score thresholds; practice assumption.
        if self.score >= 90:
            return "Merit List"
        elif self.score >= 60:
            return "Waiting List"
        return "Not Eligible"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.applicant_name} | {self.application_id} | {self.entrance_examination_score} | {self.category()}"


class College:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = College()

for _ in range(n):
    parts = input().split(",")
    applicant_name = parts[0]
    application_id = parts[1]
    entrance_examination_score = int(parts[2])
    obj.add(Applicant(applicant_name, application_id, entrance_examination_score))

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
