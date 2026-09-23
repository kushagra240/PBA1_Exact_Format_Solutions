# ============================================================
# EXACT SCREENSHOT REFERENCE
# ============================================================
# The screenshots contain TWO SEPARATE online-judge questions.
# Copy only the requested block when submitting.
#
# Screenshot Q1: Apartment Maintenance Management System (OOP)
# Screenshot Q2: Event Registration Management System - Coin Change Fewest Coins
# ============================================================

# ---------------- SCREENSHOT Q1 ----------------
class Resident:
    def __init__(self, resident_name, flat_number, maintenance_fee):
        self.resident_name = resident_name
        self.flat_number = flat_number
        self.maintenance_fee = maintenance_fee

    def status(self):
        if self.maintenance_fee >= 1:
            return "Paid"
        return "Pending"

    def display(self):
        print(self)

    def __str__(self):
        return f"{self.resident_name} | {self.flat_number} | {self.maintenance_fee} | {self.status()}"


class Society:
    def __init__(self):
        self.residents = []

    def add_resident(self, resident):
        self.residents.append(resident)

    def display_all(self):
        for resident in self.residents:
            resident.display()


n = int(input())
society = Society()

for _ in range(n):
    parts = input().split(",")
    resident_name = parts[0]
    flat_number = parts[1]
    maintenance_fee = int(parts[2])
    society.add_resident(Resident(resident_name, flat_number, maintenance_fee))

society.display_all()


# ---------------- SCREENSHOT Q2 ----------------
# Comment/remove the Q1 block before running this block separately.

c = int(input())
coins = list(map(int, input().split()))
amount = int(input())

dp = [amount + 1] * (amount + 1)
dp[0] = 0

for value in range(1, amount + 1):
    for coin in coins:
        if coin <= value:
            dp[value] = min(dp[value], dp[value - coin] + 1)

print(-1 if dp[amount] == amount + 1 else dp[amount])
