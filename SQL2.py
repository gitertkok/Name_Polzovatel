import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT
)              """)
conn.commit()

cursor.execute("INSERT INTO students (name, age, email) VALUES (?, ?, ?)", 
               ("Азамат", 14, "azamat@example.com"))
cursor.execute("INSERT INTO students (name, age, email) VALUES (?, ?, ?)", 
               ("Малика", 17, "malika@example.com"))


cursor.execute("SELECT name FROM students")
names = cursor.fetchall()

for name in names:
    print(name[0])

cursor.execute("SELECT * FROM students WHERE age > 15")
for row in cursor.fetchall():
    print(row)

conn.close()



