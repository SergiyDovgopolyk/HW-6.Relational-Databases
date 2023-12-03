import psycopg2

conn_params = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "14021992",
    "host": "localhost",
    "port": 5432
}

def create_db():
    # читаємо файл зі скриптом для створення БД
    with open('creating_db.sql', 'r') as f:
        sql = f.read()

    # створюємо з'єднання з БД
    with psycopg2.connect(**conn_params) as con:
        cur = con.cursor()
        # виконуємо скрипт із файлу, який створить таблиці в БД
        cur.execute(sql)

if __name__ == "__main__":
    create_db()
