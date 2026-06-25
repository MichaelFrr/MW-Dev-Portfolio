import psycopg2


def execute_write_query(query, data_tuple):
    try:
        connection = psycopg2.connect(
            database="Bank_DB", user="postgres", password="0", host="localhost", port=5432
        )
        cursor = connection.cursor()

        cursor.execute(query, data_tuple)
        connection.commit()
        print("Database write successful!")

    except Exception as error:
        print(f"Error while writing to database: {error}")
        if 'connection' in locals():
            connection.rollback()

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()


def execute_read_query(query, data_tuple=(), method="fetch_all", row_num=None):
    result = None
    try:

        connection = psycopg2.connect(
            database="Bank_DB", user="postgres", password="0", host="localhost", port=5432
        )
        cursor = connection.cursor()

        cursor.execute(query, data_tuple)
        if method == "fetch_all":
            result = cursor.fetchall()
        elif method in ("fetch_one", "fetch_row"):

            raw_row = cursor.fetchone()
            if raw_row is not None:
                if method == "fetch_row" and raw_row is not None:
                    result = raw_row[row_num]
                else:
                    result = raw_row
            else:
                result = None
        print("Database read successful!")
        return result

    except Exception as error:
        print(f"Error while reading from database: {error}")
        if 'connection' in locals():
            connection.rollback()
        return None
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()
