import sqlite3
from datetime import date

db = sqlite3.connect("expenses.db")
db.execute(
    "CREATE TABLE IF NOT EXISTS expenses "
    "(day TEXT, category TEXT, amount REAL)"
)

while True:
    print("\n1. Add expense")
    print("2. View expenses")
    print("3. Total expenses")
    print("4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        category = input("Category: ")
        try:
            amount = float(input("Amount INR: "))
            if not 0 < amount < float("inf"):
                raise ValueError
        except ValueError:
            print("Invalid amount")
            continue
        db.execute(
            "INSERT INTO expenses VALUES (?, ?, ?)",
            (date.today().isoformat(), category, amount)
        )
        db.commit()
        print("Expense saved!")

    elif choice == "2":
        for row in db.execute("SELECT * FROM expenses"):
            print(row)

    elif choice == "3":
        total = db.execute(
            "SELECT COALESCE(SUM(amount),0) FROM expenses"
        ).fetchone()[0]
        print("Total INR:", round(total, 2))

    elif choice == "4":
        break

db.close()
