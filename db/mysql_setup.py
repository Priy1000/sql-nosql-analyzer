import mysql.connector
import pandas as pd

def load_to_mysql():
    data = pd.read_csv("books.csv")

    conn = mysql.connector.connect(
        host="localhost", user="root", password="forPl@cement"
    )
    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS books_db")
    cursor.execute("USE books_db")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        book_id INT PRIMARY KEY,
        title VARCHAR(255),
        author VARCHAR(255),
        genre VARCHAR(255),           
        year INT
    )
    """)

    for _, row in data.iterrows():
        cursor.execute("INSERT INTO books (book_id, title, author, year) VALUES (%s, %s, %s, %s)",
                       (int(row.book_id), row.title, row.author, int(row.year)))
    
    conn.commit()
    conn.close()
    print(" MySQL Loaded")

if __name__ == "__main__":
    load_to_mysql()
