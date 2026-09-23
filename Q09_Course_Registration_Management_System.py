# 9. Course Registration Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Course:
    def __init__(self, course_name, course_code, course_fee):
        self.course_name = course_name
        self.course_code = course_code
        self.course_fee = course_fee

    def display(self):
        print(self)

    def __str__(self):
        return f"{self.course_name} | {self.course_code} | {self.course_fee}"


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
    course_name = parts[0]
    course_code = parts[1]
    course_fee = int(parts[2])
    obj.add(Course(course_name, course_code, course_fee))

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
