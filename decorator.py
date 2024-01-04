import pyodbc
import time


def timed(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        val = function(*args, **kwargs)
        end = time.time()
        f_name = function.__name__
        print(f"{f_name} took {end - start} seconds to execute!")
        return val
    return wrapper


@timed
def insert_into_db(fname, lname, gender, age):
    connection_string = 'DRIVER={SQL Server};SERVER=db_server;DATABASE=Students;UID=sa;PWD=123456'
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    try:
        # __tablename__ = 'students'
        first_name = fname
        last_name = lname
        gender = gender
        age = age

        insert_query = "INSERT INTO students (first_name, last_name, gender, age) VALUES (?, ?, ?, ?)"
        cursor.execute(insert_query, first_name, last_name, gender, age)
        conn.commit()

        print("Data inserted successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()


insert_into_db("Dave", "Johnson", "male", 39)