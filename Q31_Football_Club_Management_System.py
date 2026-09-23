# 31. Football Club Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Player:
    def __init__(self, player_name, jersey_number, total_goals_scored):
        self.player_name = player_name
        self.jersey_number = jersey_number
        self.total_goals_scored = total_goals_scored

    def category(self):
        # PDF gives names but no goal thresholds; practice assumption.
        if self.total_goals_scored >= 50:
            return "Star Player"
        elif self.total_goals_scored >= 20:
            return "Regular Player"
        return "Beginner"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.player_name} | {self.jersey_number} | {self.total_goals_scored} | {self.category()}"


class Club:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = Club()

for _ in range(n):
    parts = input().split(",")
    player_name = parts[0]
    jersey_number = int(parts[1])
    total_goals_scored = int(parts[2])
    obj.add(Player(player_name, jersey_number, total_goals_scored))

obj.display_all()

# ============================================================
# CO2 - Dynamic Programming
# ============================================================

# CO2 - Dynamic Programming: Rod Cutting
# Input: N / N prices for lengths 1..N
n = int(input())
prices = list(map(int, input().split()))
dp = [0] * (n + 1)
for length in range(1, n + 1):
    for cut in range(1, length + 1):
        dp[length] = max(dp[length], prices[cut - 1] + dp[length - cut])
print(dp[n])
