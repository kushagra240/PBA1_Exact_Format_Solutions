# 30. Cricket Team Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Player:
    def __init__(self, player_name, jersey_number, total_runs_scored):
        self.player_name = player_name
        self.jersey_number = jersey_number
        self.total_runs_scored = total_runs_scored

    def category(self):
        # PDF gives names but no run thresholds; practice assumption.
        if self.total_runs_scored >= 1000:
            return "Excellent"
        elif self.total_runs_scored >= 500:
            return "Good"
        return "Average"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.player_name} | {self.jersey_number} | {self.total_runs_scored} | {self.category()}"


class Team:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = Team()

for _ in range(n):
    parts = input().split(",")
    player_name = parts[0]
    jersey_number = int(parts[1])
    total_runs_scored = int(parts[2])
    obj.add(Player(player_name, jersey_number, total_runs_scored))

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
