import sqlite3

conn = sqlite3.connect("student.sqlite")
cursor = conn.cursor()

select_students = """
SELECT id, firstname, lastname
FROM students
WHERE age >= 15"""

cursor.execute(select_students)
first_student = cursor.fetchone()
more_students = cursor.fetchmany(10)
other_students = cursor.fetchall()

print(first_student)
print(more_students)
print(other_students)

average_query = """ 
SELECT avg(age) 
FROM students 
WHERE gender = ? 
"""
average_age = cursor.execute(average_query, ('female',)).fetchone()[0]

print(average_age)

group_by_query = """ 
SELECT gender, avg(age) 
FROM students 
GROUP BY gender 
"""
average_age_by_gender = cursor.execute(group_by_query).fetchall()

print(average_age_by_gender)

firstname_J = """
SELECT firstname, lastname
FROM students
WHERE firstname LIKE 'J%'
"""

firstname_J_5 = cursor.execute(firstname_J).fetchmany(5)
print(firstname_J_5)

sum_gender = """ 
SELECT gender, sum(age/age)
FROM students 
GROUP BY gender 
"""
number_by_gender = cursor.execute(sum_gender).fetchall()
print(number_by_gender)

conn.close()
