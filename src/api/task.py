from flask_restful import Resource, reqparse
from datetime import datetime

from .tasks import task_tuple_to_object

# from db.tasks.create_task import create_task
from db.tasks.get_task import get_task
from db.tasks.delete_task import delete_task


class Task(Resource):
  def get(self, id):
    return task_tuple_to_object(get_task(id))
  
  def delete(self, id):
    return task_tuple_to_object(delete_task(id))