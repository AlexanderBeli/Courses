import sqlite3


class Person:
    def __init__(self, first=None, last=None, age=None):
        self.first = first
        self.last = last
        self.age = age

    def clone_person(self, result):
        self.first = result[0]
        self.last = result[1]
        self.age = result[2]


conn = sqlite3.connect("mydata.db")
c = conn.cursor()

# c.execute( """CREATE TABLE persons (
#                     first_name TEXT,
#                     last_name TEXT,
#                     age INTEGER
#                     )""" )
# c.execute("""INSERT INTO persons VALUES
#                 ('John', 'Smith', 25),
#                 ('Anna', 'Smith', 30),
#                 ('Mike', 'Johnson', 40)""")

c.execute(
    """SELECT * FROM persons 
            WHERE last_name = 'Smith'"""
)
for x in c.fetchall():
    person1 = Person()
    person1.clone_person(x)
    print(person1.first)
    print(person1.last)
    print(person1.age)

# person2 = Person("Bob", "Davis", 23)
# c.execute("""INSERT INTO persons VALUES
#         ('{}', '{}', '{}')""".format(person2.first, person2.last, person2.age))

# person2 = Person("Julia", "Johnson", 28)
# c.execute("INSERT INTO persons VALUES (?, ?, ?)",
#           (person2.first, person2.last, person2.age))

c.execute("SELECT * FROM persons")
print(c.fetchall())

conn.commit()
conn.close()
