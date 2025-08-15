import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('myapi.db')
cursor = conn.cursor()

# 테이블 목록 보기
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("=== 테이블 목록 ===")
for table in tables:
    print(f"- {table[0]}")

print("\n=== Question 테이블 ===")
cursor.execute("SELECT * FROM question")
questions = cursor.fetchall()
for row in questions:
    print(row)

print("\n=== Answer 테이블 ===")
cursor.execute("SELECT * FROM answer")
answers = cursor.fetchall()
for row in answers:
    print(row)

conn.close()