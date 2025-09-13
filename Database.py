import sqlite3
conn = sqlite3.connect('learning_app.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    name TEXT,
    syllabus TEXT,
    last_login TEXT,
    streak INTEGER DEFAULT 0
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS quizzes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    option_a TEXT,
    option_b TEXT,
    option_c TEXT,
    option_d TEXT,
    correct_option TEXT
)
''')

c.execute('''
INSERT INTO quizzes (question, option_a, option_b, option_c, option_d, correct_option)
VALUES ("What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", "C")
''')

conn.commit()
conn.close()