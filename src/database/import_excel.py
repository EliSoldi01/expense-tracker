import pandas as pd
import sqlite3
import os

# DB connection
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DB_PATH = os.path.join(BASE_DIR, "db", "expense-tracker.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# load excel
df = pd.read_excel("transactions.xlsx")

# helper: category lookup cache (IMPORTANT for performance)
category_cache = {}

def get_category_id(name):
    if name in category_cache:
        return category_cache[name]

    cursor.execute('SELECT id FROM "categories" WHERE name = ?', (name,))
    result = cursor.fetchone()

    if result is None:
        print(f"⚠️ Categoria non trovata: {name}")
        return None

    category_cache[name] = result[0]
    return result[0]

# iterate rows
for _, row in df.iterrows():

    # 1. type mapping
    t_type = row["Type"].strip().lower()

    # 2. amount cleanup (€ → float)
    amount_raw = row["Amount"]

    if isinstance(amount_raw, str):
        amount = (
            amount_raw
            .replace("€", "")
            .replace(".", "")
            .replace(",", ".")
            .strip()
        )
    else:
        amount = float(amount_raw)

    amount = float(amount)

    # 3. date
    date = pd.to_datetime(row["Date"]).strftime("%Y-%m-%d")

    # 4. category
    category_name = row["Category"].strip()
    category_id = get_category_id(category_name)

    if category_id is None:
        continue

    # 5. description
    description = row["Description"] if pd.notna(row["Description"]) else None

    # 6. insert
    cursor.execute("""
        INSERT INTO "transactions" (type, date, amount, category_id, description)
        VALUES (?, ?, ?, ?, ?)
    """, (t_type, date, amount, category_id, description))

# commit
conn.commit()
conn.close()

print("✅ Import completato")