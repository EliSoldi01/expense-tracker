from fastapi import FastAPI, HTTPException, status, Path
from src.schemas.schemas import TransactionCreate, TransactionUpdate

# CRUD operations: HTTP requests
# Create: POST
# Read: GET
# Update: PUT
# Delete: DELETE

# Crate FastAPI instance -> web application
app = FastAPI()

# Endpoint  (URL)
# When user calls the root endpoint (GET), execute the root function and return a JSON response with status "ok"
@app.get("/") # Decorator to define landing page
def root():
    return {"status": "ok",
            "message": "Welcome to the Expense Tracker API!"}

# Connect to database and initialize models here
import src.database.repository as repo
from src.database.create_database import DB_PATH
import sqlite3

# Get all transactions
@app.get("/transactions")
def get_transactions(
    type: str = None,
    date: str = None,
    category: str = None, 
    start_date: str = None,
    end_date: str = None 
):
    conn = sqlite3.connect(DB_PATH)

    transactions = repo.get_transactions(conn, type, date, category, start_date, end_date)

    conn.close()

    return transactions

# Get transaction by ID
@app.get("/transactions/{id}")
def get_transaction_by_id(id: int = Path(..., description="The ID of the transaction to retrieve")):
    conn = sqlite3.connect(DB_PATH)
    transaction = repo.get_transaction_by_id(conn, id)

    if not transaction:
        conn.close()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Transaction not found")

    return transaction

# POST
@app.post("/transactions")
def add_transaction(transaction: TransactionCreate):
    conn = sqlite3.connect(DB_PATH)

    category = repo.get_category_by_name(conn, transaction.category)

    if category is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Category not found")

    new_transaction = repo.create_transaction(
        conn,
        transaction.type.value,
        transaction.date,
        transaction.amount,
        category[0],
        transaction.description
    )

    conn.close()

    return new_transaction

# PUT
@app.put("/transactions/{id}")
def update_transaction(
    t: TransactionUpdate,
    id: int = Path(..., description="The ID of the transaction to update.")
):

    conn = sqlite3.connect(DB_PATH)

    transaction = repo.get_transaction_by_id(conn, id)
    if transaction is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Transaction not found")

    category = repo.get_category_by_name(conn, t.category)
    if category is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Category not found")

    updated_transaction = repo.update_transaction(
        conn,
        id,
        t.type.value,
        t.date,
        t.amount,
        category[0],
        t.description
    )

    conn.close()
    return updated_transaction

# DELETE
@app.delete("/transactions/{id}")
def delete_transaction(id: int = Path(..., description = "The ID of the transaction to delete.")):
    conn = sqlite3.connect(DB_PATH)

    deleted_rows = repo.delete_transaction

    if deleted_rows == 0:
        raise HTTPException(404, "Transaction not found")
    
    return {
    "message": "Transaction deleted",
    "id": id
    }

###### TO DO:
# 