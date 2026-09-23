# 23. Airline Reservation Management System
# CO1 - Object-Oriented Programming
# Input: N, then N records separated by commas (no prompts).
# Output: one line per record using " | " separators.

class Passenger:
    def __init__(self, passenger_name, flight_number, ticket_fare):
        self.passenger_name = passenger_name
        self.flight_number = flight_number
        self.ticket_fare = ticket_fare

    def category(self):
        # PDF gives class names but no fare threshold; practice assumption.
        return "Business Class" if self.ticket_fare >= 5000 else "Economy Class"
    def display(self):
        print(self)

    def __str__(self):
        return f"{self.passenger_name} | {self.flight_number} | {self.ticket_fare} | {self.category()}"


class Airline:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)

    def display_all(self):
        for record in self.records:
            record.display()


n = int(input())
obj = Airline()

for _ in range(n):
    parts = input().split(",")
    passenger_name = parts[0]
    flight_number = parts[1]
    ticket_fare = int(parts[2])
    obj.add(Passenger(passenger_name, flight_number, ticket_fare))

obj.display_all()

# ============================================================
# CO2 - Dynamic Programming
# ============================================================

# CO2 - Dynamic Programming: House Robber
# Input: N / N house values
n = int(input())
values = list(map(int, input().split()))
prev2 = 0
prev1 = 0
for value in values:
    current = max(prev1, prev2 + value)
    prev2 = prev1
    prev1 = current
print(prev1)
