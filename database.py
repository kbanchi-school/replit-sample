from peewee import *

db = SqliteDatabase('people.db')


class Person(Model):
    name = CharField()

    class Meta:
        database = db


db.create_tables([Person])
Person.create(name="Keisuke")
