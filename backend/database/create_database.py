import sqlite3
import os

# Prendi 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DB_PATH = os.path.join(BASE_DIR, "backend", "database", "expense-tracker.db")

# check if database file exists
if not os.path.exists(DB_PATH):
    # Create a new database file
    open(DB_PATH, 'w').close()
    print(f"Database created at {DB_PATH}")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create a new table for transactions
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS "transactions" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "type" TEXT NOT NULL,
        "date" DATE NOT NULL,  
        "amount" REAL NOT NULL CHECK(amount > 0),
        "category_id" INTEGER NOT NULL,
        "description" TEXT,
        FOREIGN KEY (category_id) REFERENCES categories(id)
        );
    '''
)

# Create a new table for categories
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS "categories" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "name" TEXT NOT NULL,
        "type" TEXT NOT NULL,
        UNIQUE(name, type)
 );
    '''
)

# List of default categories
categories = [
    ("Rent", "expense"),
    ("Utilities", "expense"),
    ("Groceries", "expense"),
    ("Healthcare", "expense"),
    ("Transportation", "expense"),
    ("Travel/Experience", "expense"),
    ("Entertainment", "expense"),
    ("Food", "expense"),
    ("Subscription", "expense"),
    ("Gifts", "expense"),
    ("Shopping", "expense"),
    ("Other expense", "expense"),
    ("Salary", "income"),
    ("Pocket money", "income"),
    ("Gift", "income"),
    ("Other income", "income")
]

# Insert default categories into the categories table
cursor.executemany("""
INSERT OR IGNORE INTO categories (name, type)
VALUES (?, ?)
""", categories)

# Commit the changes and close the connection
print("Database and tables created successfully, and default categories inserted.")
conn.commit()
conn.close()