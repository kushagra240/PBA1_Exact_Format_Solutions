# 40. Digital Library Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class EBook:
    def __init__(self, book_title, author_name, file_size_mb):
        self.book_title = book_title
        self.author_name = author_name
        self.file_size_mb = file_size_mb

    def category(self):
        # PDF gives names but no file-size thresholds; practice assumption.
        if self.file_size_mb >= 100:
            return "Large"
        elif self.file_size_mb >= 50:
            return "Medium"
        return "Small"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.book_title} | {self.author_name} | {self.file_size_mb} | {self.category()}"


class DigitalLibrary:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = DigitalLibrary()

for _ in range(n):
    parts = input().split(",")
    book_title = parts[0]
    author_name = parts[1]
    file_size_mb = float(parts[2])
    obj.add(EBook(book_title, author_name, file_size_mb))

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
