# 35. Newspaper Subscription Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Subscriber:
    def __init__(self, subscriber_name, subscription_id, subscription_fee):
        self.subscriber_name = subscriber_name
        self.subscription_id = subscription_id
        self.subscription_fee = subscription_fee

    def category(self):
        # PDF gives names but no fee thresholds; practice assumption.
        if self.subscription_fee >= 10000:
            return "Annual"
        elif self.subscription_fee >= 5000:
            return "Half-Yearly"
        return "Monthly"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.subscriber_name} | {self.subscription_id} | {self.subscription_fee} | {self.category()}"


class Agency:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = Agency()

for _ in range(n):
    parts = input().split(",")
    subscriber_name = parts[0]
    subscription_id = parts[1]
    subscription_fee = int(parts[2])
    obj.add(Subscriber(subscriber_name, subscription_id, subscription_fee))

obj.display_all()

# ============================================================
# CO2 - Dynamic Programming
# ============================================================

# CO2 - Dynamic Programming: Fibonacci using Tabulation (Bottom-Up)
n = int(input())
if n <= 0:
    print()
elif n == 1:
    print(0)
else:
    dp = [0] * n
    dp[1] = 1
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(*dp)
