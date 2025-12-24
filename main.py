import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",          # your MySQL username
    password="",  # your MySQL password
    database="python_mysql"     # your database name
)

cursor = conn.cursor()

# Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT
)
""")

# Insert data
sql = "INSERT INTO students (name, age) VALUES (%s, %s)"
values = ("Alice", 15)
cursor.execute(sql, values)

conn.commit()  # save changes

# Read data
cursor.execute("SELECT * FROM students")
result = cursor.fetchall()

for row in result:
    print(row)

# Close connection
cursor.close()
conn.close()