from faker import Faker
import psycopg2
import random


def insert_fake_data():
    fake = Faker('uk_UA')

    conn_params = {
        "dbname": "postgres",
        "user": "postgres",
        "password": "14021992",
        "host": "localhost",
        "port": 5432
    }

    conn = psycopg2.connect(**conn_params)
    cur = conn.cursor()

    # Заповнення груп
    for _ in range(3):
        group_name = fake.word()
        cur.execute("INSERT INTO groups (group_name) VALUES (%s)", (group_name,))

    conn.commit()

    # Заповнення викладачів
    for _ in range(5):
        first_name = fake.first_name()
        last_name = fake.last_name()
        cur.execute("INSERT INTO teachers (first_name, last_name) VALUES (%s, %s)", (first_name, last_name))

    conn.commit()

    # Заповнення предметів
    for _ in range(8):
        subject_name = fake.word()
        cur.execute("INSERT INTO subjects (subject_name, teacher_id) VALUES (%s, %s)", (subject_name, random.randint(1, 5)))
        conn.commit()

        # Отримання списку student_ids
        cur.execute("SELECT id FROM students")
        student_ids = [record[0] for record in cur.fetchall()]

        # Заповнення оцінок для кожного студента з усіх предметів
        for student_id in student_ids:
            for _ in range(20):
                grade = round(random.uniform(60, 100), 2)
                subject_id = random.randint(1, 8)
                cur.execute("INSERT INTO grades (student_id, subject_id, grade) VALUES (%s, %s, %s)", (student_id, subject_id, grade))

        conn.commit()
        conn.close()

        if __name__ == "__main__":
            insert_fake_data()