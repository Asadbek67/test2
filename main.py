import psycopg2

conn = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="907786789",
        dbname="test"
    )

cursor = conn.cursor()

cursor.execute("""
    DROP TABLE IF EXISTS students
""")
cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id SERIAL PRIMARY KEY,
@@ -28,31 +24,26 @@
cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)", ('Vali', 22, 90))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)", ('Oleg', 20, 75))
""")
# select
cursor.execute("""
    SELECT name, grade 
    FROM students 
    WHERE age > 21
               """)

cursor.execute("""create table if not exists coursees (
        id serial PRIMARY KEY,
        student_id INTEGER,
        courses_name VARCHAR(50),
        )
""")

# Alining yoshini 90 ga yangilash
cursor.execute("""
    UPDATE students 
    SET grade = %s 
    WHERE name = %s
""", (90, 'Ali'))
# Reytingi 80 dan past bo'lgan talabalarni o'chirish
cursor.execute("""
    DELETE FROM students
    WHERE grade < 80
""")

# Jadvalga 'email' ustunini qo'shish
cursor.execute("""
    ALTER TABLE students
    ADD COLUMN email VARCHAR(100)
""")

# joinlar 
cursor.execute(""" SELECT students.name AS student_name, courses.course_name
FROM students
JOIN student_courses ON students.student_id = student_courses.student_id
JOIN courses ON student_courses.course_id = courses.course_id;
""")








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





