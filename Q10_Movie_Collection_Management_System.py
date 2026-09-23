# 10. Movie Collection Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Movie:
    def __init__(self, movie_name, rating, ticket_price):
        self.movie_name = movie_name
        self.rating = rating
        self.ticket_price = ticket_price

    def category(self):
        if self.rating >= 8:
            return "Blockbuster"
        elif self.rating >= 6:
            return "Hit"
        return "Average"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.movie_name} | {self.rating} | {self.ticket_price} | {self.category()}"


class Collection:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = Collection()

for _ in range(n):
    parts = input().split(",")
    movie_name = parts[0]
    rating = float(parts[1])
    ticket_price = int(parts[2])
    obj.add(Movie(movie_name, rating, ticket_price))

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
