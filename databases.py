import sqlite3
from faker import Faker
import random

# Create a connection to a database - if one does not exist, a new one will be created
conn = sqlite3.connect("student.sqlite")

# A cursor is a pointer to a place in the database which allows access
# to a table row-by-row
cursor = conn.cursor()

# SQL commands can be written as text and then 'run' using an execute command
# Example - creating a table
create_students_table = """ 
CREATE TABLE IF NOT EXISTS students ( 
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  firstname TEXT NOT NULL, 
  lastname TEXT NOT NULL, 
  age INTEGER, 
  gender TEXT 
); 
"""

insert_query = """
INSERT INTO 
students(firstname, lastname, age, gender)
VALUES ("Hermione","Granger",14,"Female");"""

cursor.execute(create_students_table)
cursor.execute(insert_query)
conn.commit()

parameterised_insert_query = """
INSERT INTO 
students(firstname, lastname, age, gender)
VALUES (?, ?, ?, ?);"""

cursor.execute(parameterised_insert_query, ("Harry", "Potter", 16, "Male"))
conn.commit()

fake = Faker('en_GB')
#random.seed(4321)
#fake.random.seed(4321)
for _ in range(10):
    f_name = fake.first_name()
    l_name = fake.last_name()
    age = random.randint(11, 18)
    gender = random.choice(('male', 'female'))
    cursor.execute(parameterised_insert_query,
                   (f_name, l_name, age, gender))
conn.commit()

#

conn.close()