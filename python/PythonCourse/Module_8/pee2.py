import os.path

from peewee import *

conn = SqliteDatabase("db_task8_2.sqlite")


class Student(Model):
    id = IntegerField(column_name="id", primary_key=True)
    name = CharField(column_name="name", max_length=32)
    surname = CharField(column_name="surname", max_length=32)
    age = IntegerField(column_name="age")
    city = CharField(column_name="city", max_length=32)

    class Meta:
        db_table = "student"
        database = conn


class Course(Model):
    id = IntegerField(column_name="id", primary_key=True)
    name = CharField(column_name="name", max_length=32)
    time_start = CharField(column_name="time_start", max_length=8)
    time_finish = CharField(column_name="time_finish", max_length=8)

    class Meta:
        db_table = "course"
        database = conn


class StudentCourse(Model):
    student_id = ForeignKeyField(Student, to_field="id")
    course_id = ForeignKeyField(Course, to_field="id")

    class Meta:
        db_table = "student_course"
        database = conn


def db_query():
    query1 = Student.select().where(Student.age > 30)

    print("Request 1")

    for query in query1:
        print(query.id, query.name, query.surname)

    query2 = (
        Student.select().join(StudentCourse).join(Course).where(Course.name == "python")
    )

    print("Request 2")

    for query in query2:
        print(query.id, query.name, query.surname)

    query3 = (
        Student.select()
        .join(StudentCourse)
        .join(Course)
        .where((Course.name == "python") & (Student.city == "Spb"))
    )

    print("Request 3")

    for query in query3:
        print(query.id, query.name, query.surname)


def db_create():
    students = [
        (1, "Max", "Brooks", 24, "Spb"),
        (2, "John", "Stones", 15, "Spb"),
        (3, "Andy", "Wings", 45, "Manchester"),
        (4, "Kate", "Brooks", 34, "Spb"),
    ]
    courses = [
        (1, "python", "21.07.21", "21.08.21"),
        (2, "java", "13.07.21", "16.08.21"),
    ]
    student_courses = [(1, 1), (2, 1), (3, 1), (4, 2)]

    Student.create_table()
    Course.create_table()
    StudentCourse.create_table()

    Student.insert_many(students).execute()
    Course.insert_many(courses).execute()
    StudentCourse.insert_many(student_courses).execute()


if not os.path.exists("db_task8_2.sqlite"):
    db_create()
db_query()
