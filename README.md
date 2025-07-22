# 📊 SQL vs NoSQL Performance Analyzer

This project compares the performance of **MySQL** and **MongoDB** by measuring the time taken to read records from both databases and displaying the results visually using Flask and Chart.js.

---

## 🚀 Features

- Reads data from both MySQL and MongoDB
- Measures time taken to fetch data from each
- Displays results in a side-by-side bar graph
- Clean HTML chart visualization (Chart.js)
- Includes sample dataset (`books.csv`) and loader scripts

---

## 🛠 Tech Stack

- **Backend**: Python, Flask
- **Databases**: MySQL, MongoDB
- **Frontend**: HTML, Chart.js
- **Data Format**: CSV

---


---

## ⚙️ Setup Instructions (LOCAL)

> 🖥️ Ensure you have Python, MySQL, and MongoDB installed locally.

### 1. Clone the repository

```bash
git clone https://github.com/your-username/sql-vs-nosql.git
cd sql-vs-nosql
```

```Install dependencies
pip install flask pandas mysql-connector-python pymongo

```

``` Load data into MySQL
python load_mysql.py

```

```Load data into MongoDB
python load_mongo.py

```

```Run the Flask App
python app.py
```
Flask will start at:
http://127.0.0.1:5000/

Available Routes:
| Route         | Description                    |
| ------------- | ------------------------------ |
| `/`           | Welcome message + routes info  |
| `/read/mysql` | Fetches records from MySQL     |
| `/read/mongo` | Fetches records from MongoDB   |
| `/compare`    | Displays time comparison graph |

Sample Output (on /compare)

