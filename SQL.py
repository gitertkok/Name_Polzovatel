import sqlite3

conn = sqlite3.connect("Mesto.db")
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

print("\n == Только имена")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)




# UPDATE обновление данных
cursor.execute("UPDATE students set age = 18 WHERE name = 'Малика'")
conn.commit()

# cursor.execute("SELECT * FROM students")
# for row in cursor.fetchall():
#     print(row)





# '''База данных - это упорядоченный набор структурированной информации или данных которые обычно 
# хранятся в электронном виде в компьютерной системе.

# SQL - это язык структурированных запросов основой задачей которого является предоставление способа 
# считывания, удаления информации в/из базы данных.
# '''

