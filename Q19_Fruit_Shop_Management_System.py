# 19. Fruit Shop Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Fruit:
    def __init__(self, fruit_name, quantity, price):
        self.fruit_name = fruit_name
        self.quantity = quantity
        self.price = price

    def display(self):
        print(self)

    def __str__(self):
        return f"{self.fruit_name} | {self.quantity} | {self.price}"


class FruitShop:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = FruitShop()

for _ in range(n):
    parts = input().split(",")
    fruit_name = parts[0]
    quantity = int(parts[1])
    price = int(parts[2])
    obj.add(Fruit(fruit_name, quantity, price))

obj.display_all()

# ============================================================
# CO2 - Dynamic Programming
# ============================================================

# CO2 - Dynamic Programming: Minimum Cost Path
# Input: rows cols / matrix rows
rows, cols = map(int, input().split())
cost = [list(map(int, input().split())) for _ in range(rows)]
for i in range(1, rows):
    cost[i][0] += cost[i - 1][0]
for j in range(1, cols):
    cost[0][j] += cost[0][j - 1]
for i in range(1, rows):
    for j in range(1, cols):
        cost[i][j] += min(cost[i - 1][j], cost[i][j - 1])
print(cost[rows - 1][cols - 1])
