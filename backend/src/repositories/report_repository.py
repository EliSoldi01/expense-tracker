def get_expenses_by_category(conn):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            c.name,
            SUM(t.amount) AS total
        FROM transactions t
        JOIN categories c ON t.category_id = c.id
        WHERE t.type = 'expense'
        GROUP BY c.name
        ORDER BY total DESC
    """)

    return cursor.fetchall()


def get_balance(conn):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            SUM(CASE WHEN type = 'income' THEN amount ELSE 0 END) AS income,
            SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END) AS expense
        FROM transactions
    """)

    return cursor.fetchone()


def get_monthly_trend(conn):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            strftime('%Y-%m', date) AS month,
            SUM(CASE WHEN type = 'income' THEN amount ELSE 0 END) AS income,
            SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END) AS expense
        FROM transactions
        GROUP BY month
        ORDER BY month
    """)

    return cursor.fetchall()


def get_top_expenses(conn, limit=10):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            t.amount,
            t.date,
            t.description,
            c.name AS category
        FROM transactions t
        JOIN categories c ON t.category_id = c.id
        WHERE t.type = 'expense'
        ORDER BY t.amount DESC
        LIMIT ?
    """, (limit,))

    return cursor.fetchall()