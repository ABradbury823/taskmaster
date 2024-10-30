from flask_restful import Resource
from db.db import Database

db = Database('test')

class Root(Resource):
  def get(self):
    return db.tables