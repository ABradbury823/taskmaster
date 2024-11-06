from flask_restful import Resource
from db.db import Database


class Teams(Resource):
  def get(self):
    db = Database('test')
    return db.tables['teams'].select()