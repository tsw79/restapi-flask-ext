from .db import db

class Movie(db.Document):
  title = db.StringField(required=True, unique=True)
  storyline = db.StringField(required=True)
  genre = db.StringField(required=True)
  release_year = db.IntField()
  runtime = db.IntField()
  # One-to-many relationship [A Movie belongs to one User | User can have many Movies]
  added_by = db.ReferenceField('User')
  meta = {'collection': 'movies'}