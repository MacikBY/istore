import sqlite3

sql ='''SELECT * FROM less_app_lessuser'''
create_tb='''CREATE TABLE students
(
    Id SERIAL PRIMARY KEY,
    name CHARACTER VARYING(30),
    age INTEGER
);'''
dr ='''DROP TABLE customers;'''
# sql ='''
# INSERT INTO students (id, name, age) VALUES (1,"Johan",25);
# '''
conn = sqlite3.connect('db.sqlite3')  # Соединяемся с базой db.sqlite3, которая лежит на "одном" уровне
cursor = conn.cursor()
# result = cursor.execute(create_tb)
conn.commit()
print(result.fetchall())
conn.close()