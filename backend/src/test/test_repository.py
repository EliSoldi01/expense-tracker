import backend.src.repositories.category_repository as c_repo
import backend.src.repositories.transaction_repository as t_repo
import backend.src.repositories.report_repository as r_repo
import sqlite3

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DB_PATH = os.path.join(BASE_DIR, "db", "expense-tracker.db")

conn = sqlite3.connect(DB_PATH)

print("TRANSACTIONS")
transactions = t_repo.get_transactions(conn)
print(transactions)

print("------------------------------")
print("CATEGORIES")
categories = c_repo.get_categories(conn)
print(categories)


