from flask_restful import Resource
from db.db import Database

class Categories(Resource):
  def get(self):
    db = Database('test')
    return db.tables['categories'].select()