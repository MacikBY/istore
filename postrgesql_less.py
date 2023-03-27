
import psycopg2

conn = psycopg2.connect(dbname="stormnet", user="postgres", password="postgres", host="127.0.0.1")
cursor = conn.cursor()

# conn.autocommit = True
# # команда для создания базы данных stormnet
# sql = "CREATE DATABASE stormnet"
#
# # выполняем код sql
# cursor.execute(sql)
# print("База данных Stormnet успешно создана")
#
# cursor.close()
# conn.close()

# создаем таблицу people
# cursor.execute("CREATE TABLE students (id SERIAL PRIMARY KEY, name VARCHAR(50),  age INTEGER)")
# # поддверждаем транзакцию
# conn.commit()
# print("Таблица people успешно создана")

# cursor.execute("INSERT INTO students (name, age) VALUES ('Johan', 25)") # добавляем строку в таблицу people
# # выполняем транзакцию
# conn.commit()
# print("Данные добавлены")
# Sara = ("Sara", 22)
# cursor.execute("INSERT INTO students (name, age) VALUES(%s, %s)", Sara)
# conn.commit()
# print("Данные добавлены")
# cursor.close()
# conn.close()
# # Добавление нескольких строк через метод .executemany
# manypeople = [("Neo", 27),("Trinity", 25),("Piphia", 55),("Morphius", 38)]
# cursor.executemany("INSERT INTO students (name, age) VALUES(%s, %s)", manypeople)
# conn.commit()
# print("Данные manypeople добавлены")
# cursor.close()
# conn.close()

# cursor.execute("SELECT * FROM students")
# for student in cursor:
#     print(f"{student[1]} - {student[2]}")
#
# cursor.close()
# conn.close()


# cursor.execute("INSERT INTO students (name, age) VALUES ('Djon', 33)") # добавляем строку в таблицу people
# # выполняем транзакцию
# conn.commit()
# print("Данные добавлены")
# cursor.close()
# conn.close()


# cursor.execute("SELECT * FROM students")
# for student in cursor.fetchall():
#     print(f"{student[1]} - {student[2]}")
#
# cursor.close()
# conn.close()

cursor.execute("ALTER TABLE students ADD COLUMN sex text")
for student in cursor.fetchall():
    print(f"{student[1]} - {student[2]}")

cursor.close()
conn.close()
# cursor.execute("DELETE FROM students WHERE name=%s", ("Biba",))
# conn.commit()
# print("Biba удален")
# cursor.close()
# conn.close()