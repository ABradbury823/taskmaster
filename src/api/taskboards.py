from flask_restful import Resource
from db.db import Database

db = Database('test')

class Taskboards(Resource):
  def get(self):
    return db.tables['taskboards'].select()