from flask_restful import Resource, reqparse
from datetime import datetime

from .tasks import task_tuple_to_object

from db.tasks.get_task import get_task
from db.tasks.update_task import update_task
from db.tasks.delete_task import delete_task


class Task(Resource):
  def get(self, id):
    return task_tuple_to_object(get_task(id))
  
  def put(self, id):
    task_parser = reqparse.RequestParser(bundle_errors=True)
    task_parser.add_argument(
      'taskboard_id', type=int, location='json', required=True, 
      help="taskboard_id is a required field"
    )
    task_parser.add_argument(
      'name', type=str, location='json', required=True, 
      help="Name is a required field"
    )
    task_parser.add_argument(
      'assignee_id', type=int, location='json', required=True,
      help='user_id of assignee'
    )
    task_parser.add_argument(
      'description', type=str, location='json',
      help='task description'
    )
    task_parser.add_argument(
      'due_date', type=lambda x: datetime.strptime(
        x,
        "%d/%m/%Y,%H:%M:%S"
      ), 
      help='When the required item is due'
    )
    args = task_parser.parse_args()
    return task_tuple_to_object(update_task(id, args))
  
  def delete(self, id):
    return task_tuple_to_object(delete_task(id))