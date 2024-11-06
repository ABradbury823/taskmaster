from flask_restful import Resource
from flask import abort
from db.db import Database


class Taskboard(Resource):
  def get(self, id):
    db = Database('test')
    res = db.tables['taskboards'].select(where={'id': id}, number=1)
    if res is None: abort(404)
    return res