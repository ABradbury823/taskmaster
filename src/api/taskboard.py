from flask_restful import Resource
from flask import abort
from db.db import Database

db = Database('test')

class Taskboard(Resource):
  def get(self, id):
    res = db.tables['taskboards'].select(where={'id': id}, number=1)
    if res is None: abort(404)
    return res