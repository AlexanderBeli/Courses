#import sqlite3
from peewee import *
from datetime import date

db = SqliteDatabase('db2.sqlite')
cursor = db.cursor()
db.close()


class Students(Model):
    #name = CharField()
    #birthday = DateField()
    id = IntegerField(column_name='id')
    name = CharField(column_name='name')
    surname = CharField(column_name='surname')
    age = IntegerField(column_name='age')
    city = CharField(column_name='city')

    class Meta:
        database = db # This model uses the "db.sqlite" database.

class Courses(Model):
    id = IntegerField(column_name='id')
    name = CharField(column_name='name')
    time_start = DateField(column_name='time_start')
    time_end = DateField(column_name='time_end')

    class Meta:
        database = db # This model uses the "db.sqlite" database.

class Student_courses(Model):
    student_id = IntegerField(column_name='student_id')
    course_id = IntegerField(column_name='course_id')

    class Meta:
        database = db # This model uses the "db.sqlite" database.

db.connect()
db.create_tables([Students, Courses, Student_courses])

student1 = Students.create(id=1, name='Max', surname='Brooks', age=24, city='Spb')
student2 = Students.create(id=2, name='John', surname='Stones', age=15, city='Spb')
student3 = Students.create(id=3, name='Andy', surname='Wings', age=45, city='Manchester')
student4 = Students.create(id=4, name='Kate', surname='Brooks', age=34, city='Spb')

Course1 = Courses.create(id=1, name='python', time_start=date(2021, 7, 21) ,time_end=date(2021, 8, 21) )
Course2 = Courses.create(id=2, name='java', time_start=date(2021, 7, 13) ,time_end=date(2021, 8, 16) )

StC1 = Student_courses.create(student_id=1, course_id=1)
StC1 = Student_courses.create(student_id=2, course_id=1)
StC1 = Student_courses.create(student_id=3, course_id=1)
StC1 = Student_courses.create(student_id=4, course_id=2)

query = Students.select().where(Students.age > 30)
for n in query:
    print(n.name)

#query =
