import csv
import random

DEPTS = ["CS", "EE", "ME", "CE"]

NUM_ROWS = 20000  # increase to 50k / 100k safely

with open("students_large.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Email", "Phone", "Year", "Dept"])

    for i in range(NUM_ROWS):
        writer.writerow([
            f"Student {i}",
            f"student{i}@example.com",
            f"9{random.randint(100000000, 999999999)}",
            random.randint(1, 5),
            random.choice(DEPTS)
        ])

print("Dataset generated:", NUM_ROWS)