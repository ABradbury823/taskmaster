from flask_restful import Resource
from db.db import Database


class Taskboards(Resource):
  def get(self):
    db = Database('test')
    return db.tables['taskboards'].select()