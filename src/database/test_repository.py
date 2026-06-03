from repository import *
import sqlite3

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DB_PATH = os.path.join(BASE_DIR, "db", "expense-tracker.db")

conn = sqlite3.connect(DB_PATH)

print("TRANSACTIONS")
transactions = get_transactions(conn)
print(transactions)

print("------------------------------")
print("TRANSACTIONS WITH CATEGORIES")
transactions_with_categories = get_transactions_with_category(conn)
print(transactions_with_categories)

print("------------------------------")
print("CATEGORIES")
categories = get_categories(conn)
print(categories)

for t in transactions:
    print(f"Deleting transaction with id {t[0]}")
    delete_transaction(conn, t[0])

