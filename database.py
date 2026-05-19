import _sqlite3


conn = _sqlite3.connect('orders.db')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT NOT NULL,
        comment TEXT
    )
""")
conn.commit()
def add_new(name,phone,email,comment):
    cursor.execute("""
        INSERT INTO orders(name,phone,email,comment)
        VALUES (?,?,?,?)
        

    """,
    (name,phone,email,comment)
    )
    conn.commit()

def get_orders(limit = None):
    if limit:
        cursor.execute(
            """
            SELECT * FROM orders
            LIMIT ?
            """,
            (limit,)
        )
        
    else:
        cursor.execute(
        """
        SELECT*FROM orders
        """),
    return cursor.fetchall()


def delete_order(order_id,):
    cursor.execute("""
        DELETE FROM orders
        WHERE id = ?
    """,
    (order_id,)
    )
    conn.commit()
    
def update_order(new_comment,order_id,):
    cursor.execute("""
        UPDATE orders
        SET comment = ?
        WHERE id = ?
        


    """,
    (new_comment,order_id,)
    )
    conn.commit()
 