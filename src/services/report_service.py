import src.repositories.report_repository as r_repo

# =========================
# BY CATEGORY
# =========================
def get_expenses_by_category_service(conn):

    rows = r_repo.get_expenses_by_category(conn)

    return [
        {
            "category": row[0],
            "total": row[1]
        }
        for row in rows
    ]


# =========================
# BALANCE
# =========================
def get_balance_service(conn):

    row = r_repo.get_balance(conn)

    income = row[0]
    expense = row[1]

    return {
        "income": income,
        "expense": expense,
        "balance": income - expense
    }


# =========================
# MONTHLY TREND
# =========================
def get_monthly_report_service(conn):

    rows = r_repo.get_monthly_trend(conn)

    return [
        {
            "month": row[0],
            "income": row[1],
            "expense": row[2]
        }
        for row in rows
    ]


# =========================
# TOP EXPENSES
# =========================
def get_top_expenses_service(conn, limit=10):

    rows = r_repo.get_top_expenses(conn, limit)

    return [
        {
            "amount": row[0],
            "date": row[1],
            "description": row[2],
            "category": row[3]
        }
        for row in rows
    ]