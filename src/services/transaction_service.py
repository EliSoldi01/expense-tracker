from fastapi import HTTPException, status

import src.repositories.transaction_repository as t_repo
import src.repositories.category_repository as c_repo


# =========================
# GET ALL
# =========================
def get_transactions_service(conn, type=None, date=None, category=None, start_date=None, end_date=None):

    return t_repo.get_transactions(
        conn,
        type,
        date,
        category,
        start_date,
        end_date
    )


# =========================
# GET BY ID
# =========================
def get_transaction_by_id_service(conn, transaction_id):

    transaction = t_repo.get_transaction_by_id(conn, transaction_id)

    if transaction is None:
        raise HTTPException(404, "Transaction not found")

    return transaction


# =========================
# CREATE
# =========================
def create_transaction_service(conn, data):

    category = c_repo.get_category_by_name(conn, data.category)

    if category is None:
        raise HTTPException(404, "Category not found")

    transaction_id = t_repo.create_transaction(
        conn,
        data.type.value,
        data.date,
        data.amount,
        category[0],
        data.description
    )

    return {"id": transaction_id}


# =========================
# UPDATE
# =========================
def update_transaction_service(conn, transaction_id, data):

    transaction = t_repo.get_transaction_by_id(conn, transaction_id)

    if transaction is None:
        raise HTTPException(404, "Transaction not found")

    category = c_repo.get_category_by_name(conn, data.category)

    if category is None:
        raise HTTPException(404, "Category not found")

    t_repo.update_transaction(
        conn,
        transaction_id,
        data.type.value,
        data.date,
        data.amount,
        category[0],
        data.description
    )

    return {"message": "updated"}


# =========================
# DELETE
# =========================
def delete_transaction_service(conn, transaction_id):

    transaction = t_repo.get_transaction_by_id(conn, transaction_id)

    if transaction is None:
        raise HTTPException(404, "Transaction not found")

    t_repo.delete_transaction(conn, transaction_id)