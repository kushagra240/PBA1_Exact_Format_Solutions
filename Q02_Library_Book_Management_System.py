# 2. Library Book Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Book:
    def __init__(self, book_title, author_name, price):
        self.book_title = book_title
        self.author_name = author_name
        self.price = price

    def category(self):
        if self.price >= 1000:
            return "Premium"
        elif self.price >= 500:
            return "Standard"
        return "Basic"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.book_title} | {self.author_name} | {self.price} | {self.category()}"


class Library:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = Library()

for _ in range(n):
    parts = input().split(",")
    book_title = parts[0]
    author_name = parts[1]
    price = int(parts[2])
    obj.add(Book(book_title, author_name, price))

obj.display_all()

# ============================================================
# CO2 - Dynamic Programming
# ============================================================

# CO2 - Dynamic Programming: Climbing Stairs
n = int(input())
if n <= 1:
    print(1)
else:
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    print(b)
