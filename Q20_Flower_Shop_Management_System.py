# 20. Flower Shop Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Flower:
    def __init__(self, flower_name, color, price):
        self.flower_name = flower_name
        self.color = color
        self.price = price

    def display(self):
        print(self)

    def __str__(self):
        return f"{self.flower_name} | {self.color} | {self.price}"


class FlowerShop:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = FlowerShop()

for _ in range(n):
    parts = input().split(",")
    flower_name = parts[0]
    color = parts[1]
    price = int(parts[2])
    obj.add(Flower(flower_name, color, price))

obj.display_all()

# ============================================================
# CO2 - Dynamic Programming
# ============================================================

# CO2 - Dynamic Programming: Edit Distance
a = input()
b = input()
prev = list(range(len(b) + 1))
for i in range(1, len(a) + 1):
    curr = [i]
    for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
            curr.append(prev[j - 1])
        else:
            curr.append(1 + min(prev[j], curr[j - 1], prev[j - 1]))
    prev = curr
print(prev[-1])
