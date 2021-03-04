from flask_mongoengine import MongoEngine

db = MongoEngine()

def init_db(app):
  app.config['MONGODB_SETTINGS'] = {
    'host': app.config['DATABASE_URI']
  }
  db.init_app(app)