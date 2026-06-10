from fastapi import FastAPI, Depends, Response
import sqlite3

import src.schemas.schemas as schema

import src.services.transaction_service as t_service
import src.services.report_service as r_service

from database.create_database import DB_PATH

app = FastAPI()

### CORS Configuration: connect frontend and backend during development
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

### Database connection dependency
def get_database_connection():
    conn = sqlite3.connect(DB_PATH)

    try:
        yield conn
    finally:
        conn.close()

# =========================
# ROOT
# =========================
@app.get("/")
def root():
    return {"status": "ok"}


# =========================
# TRANSACTIONS - GET ALL
# =========================
@app.get("/transactions")
def get_transactions(
    conn = Depends(get_database_connection),
    type: str = None,
    date: str = None,
    category: str = None,
    start_date: str = None,
    end_date: str = None
):

    data = t_service.get_transactions_service(
        conn,
        type=type,
        date=date,
        category=category,
        start_date=start_date,
        end_date=end_date
    )

    conn.close()
    return data


# =========================
# TRANSACTION BY ID
# =========================
@app.get("/transactions/{id}")
def get_transaction_by_id(id: int, conn = Depends(get_database_connection)):

    data = t_service.get_transaction_by_id_service(conn, id)

    conn.close()
    return data

# =========================
# LAST N TRANSACTIONS
# =========================
@app.get("/transactions/last/{limit}")
def last_transactions(limit: int, conn = Depends(get_database_connection)):

    data = t_service.get_last_transactions_service(conn, limit)

    return data


# =========================
# CREATE
# =========================
@app.post("/transactions")
def create_transaction(transaction: schema.TransactionCreate, conn = Depends(get_database_connection)):

    result = t_service.create_transaction_service(conn, transaction)

    return result


# =========================
# UPDATE
# =========================
@app.put("/transactions/{id}")
def update_transaction(id: int, t: schema.TransactionUpdate, conn = Depends(get_database_connection)):

    result = t_service.update_transaction_service(conn, id, t)

    return result


# =========================
# DELETE
# =========================
@app.delete("/transactions/{id}", status_code=204)
def delete_transaction(id: int, conn = Depends(get_database_connection)):

    t_service.delete_transaction_service(conn, id)

    return Response(status_code=204)


# =========================
# REPORTS
# =========================
@app.get("/reports/by-category")
def by_category(conn = Depends(get_database_connection)):

    data = r_service.get_expenses_by_category_service(conn)

    return data


@app.get("/reports/balance")
def balance(conn = Depends(get_database_connection)):

    data = r_service.get_balance_service(conn)

    return data


@app.get("/reports/monthly-trend")
def monthly_trend():

    conn = sqlite3.connect(DB_PATH)

    data = r_service.get_monthly_report_service(conn)

    conn.close(conn = Depends(get_database_connection))
    return data


@app.get("/reports/top-expenses/{limit}")
def top_expenses(limit: int, conn = Depends(get_database_connection)):

    data = r_service.get_top_expenses_service(conn, limit)

    return data


