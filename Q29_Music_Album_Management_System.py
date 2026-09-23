# 29. Music Album Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Album:
    def __init__(self, album_name, singer_name, price):
        self.album_name = album_name
        self.singer_name = singer_name
        self.price = price

    def category(self):
        # PDF gives names but no price thresholds; practice assumption.
        if self.price >= 2000:
            return "Platinum"
        elif self.price >= 1000:
            return "Gold"
        return "Silver"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.album_name} | {self.singer_name} | {self.price} | {self.category()}"


class MusicLibrary:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = MusicLibrary()

for _ in range(n):
    parts = input().split(",")
    album_name = parts[0]
    singer_name = parts[1]
    price = int(parts[2])
    obj.add(Album(album_name, singer_name, price))

obj.display_all()

# ============================================================
# CO2 - Dynamic Programming
# ============================================================

# CO2 - Dynamic Programming: Longest Common Substring
a = input()
b = input()
dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
best = 0
for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            best = max(best, dp[i][j])
print(best)
