import psycopg2

conn = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="907786789",
        dbname="test"
    )


cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            age INTEGER,
            grade integer
        )
    ''')


cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s,%s)", ('Ali', 21, 85))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)", ('Vali', 22, 90))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)", ('Oleg', 20, 75))

cursor.execute("""create table if not exists coursees (
        id serial PRIMARY KEY,
        student_id INTEGER,
        courses_name VARCHAR(50),
        )
""")


cursor.execute(""" SELECT students.name AS student_name, courses.course_name
FROM students
JOIN student_courses ON students.student_id = student_courses.student_id
JOIN courses ON student_courses.course_id = courses.course_id;






""")



conn.commit()