def create_category(conn, name, type):
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO categories (name, type)
        VALUES (?, ?)
    """, (name, type))

    conn.commit()

    return cursor.lastrowid


def get_categories(conn):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, type
        FROM categories
    """)

    return cursor.fetchall()


def get_category_by_name(conn, name):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, type
        FROM categories
        WHERE name = ?
    """, (name,))

    return cursor.fetchone()


def update_category(conn, category_id, name, type):
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE categories
        SET name = ?, type = ?
        WHERE id = ?
    """, (name, type, category_id))

    conn.commit()


def delete_category(conn, category_id):
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM categories
        WHERE id = ?
    """, (category_id,))

    conn.commit()

    return cursor.rowcount