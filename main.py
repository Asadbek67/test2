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

# select
cursor.execute("""
    SELECT name, grade 
    FROM students 
    WHERE age > 21
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


conn.commit()