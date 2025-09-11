import mysql.connector
from mysql.connector import Error

def main():
    # Database connection configuration
    db_config = {
        "host": "localhost",
        "user": "test",
        "password": "new_password",
        "database": "testdb"
    }

    try:
        # Using context manager for automatic connection handling
        with mysql.connector.connect(**db_config) as conn:
            # Create cursor with dictionary=True to get results as dictionaries
            with conn.cursor(dictionary=True) as cursor:
                try:
                    # Create table if not exists
                    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS products (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            name VARCHAR(100),
                            price DECIMAL(10,2)
                        )
                    """)
                    print("Table 'products' created/verified successfully")

                    # Insert multiple records using executemany
                    products = [
                        ("Laptop", 999.99),
                        ("Mouse", 19.99),
                        ("Keyboard", 49.99),
                        ("Monitor", 199.99)
                    ]
                    cursor.executemany(
                        "INSERT INTO products (name, price) VALUES (%s, %s)",
                        products
                    )
                    print(f"Inserted {cursor.rowcount} records")

                    # Commit the transaction
                    conn.commit()
                    print("Transaction committed")

                    # Query all records
                    print("\nAll products:")
                    cursor.execute("SELECT * FROM products")
                    for row in cursor:
                        print(f"ID: {row['id']}, Name: {row['name']}, Price: {row['price']}")

                    # Conditional query
                    print("\nProducts under $50:")
                    cursor.execute("SELECT * FROM products WHERE price < %s", (50,))
                    for row in cursor:
                        print(f"{row['name']}: ${row['price']}")

                except Error as e:
                    # Rollback in case of error
                    conn.rollback()
                    print(f"Database error occurred: {e}")
                except Exception as e:
                    conn.rollback()
                    print(f"Unexpected error: {e}")

    except Error as e:
        print(f"Failed to connect to MySQL: {e}")
    except Exception as e:
        print(f"General error occurred: {e}")

    # Connection automatically closes when exiting the with block
if __name__ == "__main__":
    main()
