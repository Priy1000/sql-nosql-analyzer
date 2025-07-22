from flask import Flask, jsonify,render_template
import time
import mysql.connector
from pymongo import MongoClient

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "message": "Welcome to the SQL vs NoSQL Benchmark App",
        "routes": ["/read/mysql", "/read/mongo"]
    })

@app.route("/read/mysql")
def read_mysql():
    start = time.time()
    conn = mysql.connector.connect(host="localhost", user="root", password="forPl@cement", database="books_db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    data = cursor.fetchall()
    conn.close()
    end = time.time()
    return jsonify({"source": "MySQL", "records": len(data), "time_taken": end - start})

@app.route("/read/mongo")
def read_mongo():
    start = time.time()
    client = MongoClient("mongodb://localhost:27017/")
    db = client["books_db"]
    data = list(db["books"].find())
    end = time.time()
    return jsonify({"source": "MongoDB", "records": len(data), "time_taken": end - start})

@app.route("/compare")
def compare():
    # Measure MySQL
    start_sql = time.time()
    conn = mysql.connector.connect(host="localhost", user="root", password="forPl@cement", database="books_db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    sql_data = cursor.fetchall()
    conn.close()
    end_sql = time.time()
    sql_time = end_sql - start_sql

    # Measure MongoDB
    start_mongo = time.time()
    client = MongoClient("mongodb://localhost:27017/")
    db = client["books_db"]
    mongo_data = list(db["books"].find())
    end_mongo = time.time()
    mongo_time = end_mongo - start_mongo

    return render_template("compare.html",
                           sql_time=round(sql_time, 5),
                           mongo_time=round(mongo_time, 5),
                           sql_count=len(sql_data),
                           mongo_count=len(mongo_data))


if __name__ == "__main__":
    app.run(debug=True)
