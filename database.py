import psycopg2
import os


conn = psycopg2.connect(
    host = os.getenv("DB_HOST"),
    database = os.getenv("DB_NAME"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"),
    port = int(os.getenv("DB_PORT")) 
    )
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id SERIAL PRIMARY KEY,
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
        VALUES (%s,%s,%s,%s)
        

    """,
    (name,phone,email,comment)
    )
    conn.commit()

def get_orders(limit = None):
    if limit:
        cursor.execute(
            """
            SELECT * FROM orders
            LIMIT %s
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
        WHERE id = %s
    """,
    (order_id,)
    )
    conn.commit()
    
def update_order(new_comment,order_id,):
    cursor.execute("""
        UPDATE orders
        SET comment = %s
        WHERE id = %s
        


    """,
    (new_comment,order_id,)
    )
    conn.commit()
 