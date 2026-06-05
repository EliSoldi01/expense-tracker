def create_transaction(conn, type, date, amount, category_id, description):
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO transactions (type, date, amount, category_id, description)
        VALUES (?, ?, ?, ?, ?)
    """, (type, date, amount, category_id, description))

    conn.commit()

    return cursor.lastrowid


def get_transactions(conn, type=None, date=None, category=None, start_date=None, end_date=None):

    cursor = conn.cursor()

    query = """
        SELECT
            t.id,
            t.type,
            t.date,
            t.amount,
            t.description,
            c.name AS category
        FROM transactions t
        LEFT JOIN categories c ON t.category_id = c.id
        WHERE 1=1
    """

    params = []

    if type:
        query += " AND t.type = ?"
        params.append(type)

    if date:
        query += " AND t.date = ?"
        params.append(date)

    if category:
        query += " AND c.name = ?"
        params.append(category)

    if start_date:
        query += " AND t.date >= ?"
        params.append(start_date)

    if end_date:
        query += " AND t.date <= ?"
        params.append(end_date)

    cursor.execute(query, params)

    return cursor.fetchall()


def get_transaction_by_id(conn, transaction_id):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            t.id,
            t.type,
            t.date,
            t.amount,
            t.description,
            c.name AS category
        FROM transactions t
        LEFT JOIN categories c ON t.category_id = c.id
        WHERE t.id = ?
    """, (transaction_id,))

    return cursor.fetchone()


def update_transaction(conn, transaction_id, type, date, amount, category_id, description):
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE transactions
        SET type = ?,
            date = ?,
            amount = ?,
            category_id = ?,
            description = ?
        WHERE id = ?
    """, (type, date, amount, category_id, description, transaction_id))

    conn.commit()


def delete_transaction(conn, transaction_id):
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM transactions
        WHERE id = ?
    """, (transaction_id,))

    conn.commit()

    return cursor.rowcount