#import sqlite3
from peewee import *
from datetime import date
import os.path

db = SqliteDatabase('db2.sqlite')

#cursor = db.cursor()
#db.close()


class Student(Model):
    id = IntegerField(column_name='id', primary_key=True)
    name = CharField(column_name='name', max_length=32)
    surname = CharField(column_name='surname', max_length=32)
    age = IntegerField(column_name='age')
    city = CharField(column_name='city', max_length=32)

    class Meta:
        #db_table = 'Student'
        database = db # This model uses the "db.sqlite" database.

class Course(Model):
    id = IntegerField(column_name='id', primary_key=True)
    name = CharField(column_name='name', max_length=32)
    time_start = DateField(column_name='time_start')
    time_end = DateField(column_name='time_end')

    class Meta:
        #db_table = 'Course'
        database = db # This model uses the "db.sqlite" database.

class Student_course(Model):
    #student_id = IntegerField(column_name='student_id')
    #course_id = IntegerField(column_name='course_id')
    student_id = ForeignKeyField(Student, to_field='id')
    course_id = ForeignKeyField(Course, to_field='id')

    class Meta:
        #db_table = 'Student_course'
        database = db # This model uses the "db.sqlite" database.

def db_create():

    db.connect()
    db.create_tables([Student, Course, Student_course])

    student1 = Student.create(id=1, name='Max', surname='Brooks', age=24, city='Spb')
    student2 = Student.create(id=2, name='John', surname='Stones', age=15, city='Spb')
    student3 = Student.create(id=3, name='Andy', surname='Wings', age=45, city='Manchester')
    student4 = Student.create(id=4, name='Kate', surname='Brooks', age=34, city='Spb')

    Course1 = Course.create(id=1, name='python', time_start=date(2021, 7, 21) ,time_end=date(2021, 8, 21) )
    Course2 = Course.create(id=2, name='java', time_start=date(2021, 7, 13) ,time_end=date(2021, 8, 16) )

    StC1 = Student_course.create(student_id=1, course_id=1)
    StC1 = Student_course.create(student_id=2, course_id=1)
    StC1 = Student_course.create(student_id=3, course_id=1)
    StC1 = Student_course.create(student_id=4, course_id=2)

def db_query():
    print('Request 1:')
    query1 = Student.select().where(Student.age > 30)
    for n in query1:
        print(n.name)

    print('Request 2:')
    query2 = (Student
              .select(Student, Student_course, Course)
              .join(Student_course)
              .join(Course)
              .where(Course.name == 'python'))
    for x in query2:
        print(x.name)

    print('Request 2:')
    query3 = (Student
              .select(Student, Student_course, Course)
              .join(Student_course)
              .join(Course)
              .where((Course.name == 'python') & (Student.city == 'Spb')))
    for k in query3:
        print(k.name)

if not os.path.exists('db2.sqlite'):
    db_create()
db_query()