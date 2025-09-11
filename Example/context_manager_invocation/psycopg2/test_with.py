import psycopg2
from psycopg2 import sql, errors
from psycopg2.extras import DictCursor

def main():
    # Database connection parameters
    db_params = {
        "dbname": "testdb",
        "user": "postgres",
        "password": "new_password",
        "host": "localhost",
        "port": "5432"
    }

    try:
        # Using context manager for automatic connection handling
        with psycopg2.connect(**db_params) as conn:
            # Disable autocommit to manually control transactions
            conn.autocommit = False

            # Using DictCursor to get results as dictionaries
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                try:
                    # 1. Create table
                    cursor.execute("""
                        DROP TABLE IF EXISTS employees;
                        CREATE TABLE employees (
                            id SERIAL PRIMARY KEY,
                            name VARCHAR(100) NOT NULL,
                            department VARCHAR(50),
                            salary NUMERIC(10, 2),
                            hire_date DATE,
                            email VARCHAR(100) UNIQUE
                        )
                    """)
                    print("Table created successfully")

                    # 2. Insert data - using parameterized queries to prevent SQL injection
                    insert_query = sql.SQL("""
                        INSERT INTO employees (name, department, salary, hire_date, email)
                        VALUES (%s, %s, %s, %s, %s)
                        RETURNING id
                    """)

                    employees = [
                        ("John Doe", "Engineering", 8500.00, "2020-05-15", "john@example.com"),
                        ("Jane Smith", "Marketing", 7500.00, "2019-11-22", "jane@example.com"),
                        ("Mike Johnson", "HR", 9000.00, "2018-03-10", "mike@example.com")
                    ]

                    for emp in employees:
                        cursor.execute(insert_query, emp)
                        emp_id = cursor.fetchone()[0]
                        print(f"Inserted employee {emp[0]}, ID: {emp_id}")

                    # 3. Update data
                    cursor.execute("""
                        UPDATE employees 
                        SET salary = salary * 1.1 
                        WHERE department = %s
                    """, ("Engineering",))
                    print(f"Updated {cursor.rowcount} records")

                    # 4. Query data
                    # 4.1 Query all
                    cursor.execute("SELECT * FROM employees ORDER BY salary DESC")
                    print("\nAll employees (sorted by salary descending):")
                    for row in cursor.fetchall():
                        print(dict(row))

                    # 4.2 Conditional query
                    cursor.execute("""
                        SELECT name, salary 
                        FROM employees 
                        WHERE salary > %s
                    """, (8000,))
                    print("\nEmployees with salary above 8000:")
                    for row in cursor.fetchall():
                        print(f"{row['name']}: {row['salary']}")

                    # 5. Commit transaction
                    conn.commit()
                    print("\nTransaction committed")

                except errors.UniqueViolation as e:
                    conn.rollback()
                    print(f"Unique constraint violation: {e}")
                except errors.DatabaseError as e:
                    conn.rollback()
                    print(f"Database error: {e}")
                except Exception as e:
                    conn.rollback()
                    print(f"Error occurred: {e}")
                    raise

            # 6. Delete operation (demonstrated in a separate transaction)
            with conn.cursor() as cursor:
                try:
                    cursor.execute("DELETE FROM employees WHERE name = %s", ("Mike Johnson",))
                    print(f"\nDeleted {cursor.rowcount} records")
                    
                    # Verify deletion
                    cursor.execute("SELECT COUNT(*) FROM employees WHERE name = %s", ("Mike Johnson",))
                    count = cursor.fetchone()[0]
                    print(f"Records count for Mike Johnson after deletion: {count}")
                    
                    conn.commit()
                except Exception as e:
                    conn.rollback()
                    print(f"Delete operation failed: {e}")

    except psycopg2.OperationalError as e:
        print(f"Failed to connect to database: {e}")
    except Exception as e:
        print(f"Error occurred: {e}")

    # Connection automatically closes when exiting the with block

if __name__ == "__main__":
    main()

