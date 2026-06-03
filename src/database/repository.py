###### TRANSACTIONS ######

## CREATE
def create_transaction(conn, type, date, amount, category_id, description):
    """Create a new transaction in the database."""
    cursor = conn.cursor()

    cursor.execute(
        '''
        INSERT INTO "transactions" (type, date, amount, category_id, description)
        VALUES (?, ?, ?, ?, ?)
        ''', (type, date, amount, category_id, description)
    )

    transaction_id = cursor.lastrowid

    conn.commit()

    return {
        "id": transaction_id,
        "type": type,
        "date": date,
        "amount": amount,
        "category_id": category_id,
        "description": description
    }

## GET
def get_transactions(conn, type, date, category_name, start_date, end_date):
    """Retrieve all transactions from the database if filters are None"""
    cursor = conn.cursor()

    query = """
    SELECT t.*
    FROM transactions t
    JOIN categories c ON t.category_id = c.id
    WHERE 1=1
    """

    params = []

    if type is not None:
        query += " AND t.type = ?"
        params.append(type)
    
    if date is not None:
        query += " AND t.date = ?"
        params.append(date)

    if category_name is not None:
        query += " AND c.name = ?"
        params.append(category_name)

    if start_date is not None:
        query += " AND t.date >= ?"
        params.append(start_date)
    
    if end_date is not None:
        query += " AND t.date <= ?"
        params.append(end_date)

    cursor.execute(query, params)

    return cursor.fetchall()

def get_transaction_by_id(conn, transaction_id):
    """Retrieve a transaction by its ID from the database."""

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM "transactions"
        WHERE id = ?
        """, (transaction_id,)
    )

    return cursor.fetchone()

def update_transaction(conn, transaction_id, type, date, amount, category_id, description):
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE transactions
        SET type = ?,
            date = ?,
            amount = ?,
            category_id = ?,
            description = ?
        WHERE id = ?
        """,
        (type, date, amount, category_id, description, transaction_id)
    )

    conn.commit()

    return {
        "id": transaction_id,
        "type": type,
        "date": date,
        "amount": amount,
        "category_id": category_id,
        "description": description
    }

def delete_transaction(conn, transaction_id):
    """Delete a transaction from the database."""
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM "transactions"
        WHERE id = ?
        """, (transaction_id,)
    )

    conn.commit()
    
    return cursor.rowcount


###### CATEGORIES ######


def create_category(conn, name, type):
    """Create a new category in the database."""
    cursor = conn.cursor()

    cursor.execute(
        '''
        INSERT OR IGNORE INTO "categories" (name, type)
        VALUES (?, ?)
        ''', (name, type)
    )

    conn.commit()

def get_categories(conn):
    """Retrieve categories from the database."""
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM "categories"  
        """
    )

    return cursor.fetchall()

def get_category_by_name(conn, name):
    cursor = conn.cursor()

    cursor.execute(
        """ 
        SELECT id FROM categories
        WHERE name = ?
        """, (name,)
    )

    result = cursor.fetchone()
    return result if result else None

def update_category(conn, category_id, name, type):
    """Update an existing category in the database."""
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE "categories"
        SET name = ?, type = ?
        WHERE id = ?
        """, (name, type, category_id)
    )

    conn.commit()

def delete_category(conn, category_id):
    """Delete a category from the database."""
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM "categories"
        WHERE id = ?
        """, (category_id,)
    )

    conn.commit()
 