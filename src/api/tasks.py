from flask_restful import Resource, reqparse
from datetime import datetime

from db.tasks.create_task import create_task
from db.tasks.get_task import get_all_tasks
from db.tasks.delete_task import delete_task

from db.db import Database

def task_tuple_to_object(task: tuple):
  return {
    "id": task[0],
    "taskboard_id": task[1],
    "assignee_id": task[2],
    "name": task[3],
    "description": task[4],
    "due_date": task[5] if task[5] is None else (task[5].strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"),
  }

class Tasks(Resource):
  def get(self):
    # return list((task_tuple_to_object(task) for task in get_all_tasks()))
    task_filter_parser = reqparse.RequestParser(bundle_errors=True)
    task_filter_parser.add_argument(
      'taskboard_id', type=int, location='args'
    )
    args = task_filter_parser.parse_args()
    where={}
    for key in args:
      if args[key] is not None: where[key] = args[key]
    db = Database('test')
    return db.tables['tasks'].select(where=where)

  def post(self):
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
      'assignee_id', type=int, location='json',
      help='user_id of assignee'
    )
    task_parser.add_argument(
      'description', type=str, location='json',
      help='task description'
    )
    task_parser.add_argument(
      'due_date', type=lambda x: datetime.strptime(
        x,
        "%Y-%m-%dT%H:%M:%S.%fZ"
      ), 
      help='When the required item is due'
    )
    args = task_parser.parse_args(strict=True)
    new_task = create_task(args.get('taskboard_id'), args)
    return task_tuple_to_object(new_task)
  
  def delete(self):
    task_parser = reqparse.RequestParser(bundle_errors=True)
    task_parser.add_argument(
      'id', type=int, action='append',
      location='args', help="id of the task"
    )
    # TODO: Implement other behavior for deletion
    # task_parser.add_argument(
    #   'taskboard_id', type=int, action='append',
    #   location='args', help="id of the taskboard"
    # )
    # task_parser.add_argument(
    #   'name', type=str, action='append',
    #   location='args', help="name of the task"
    # )
    # task_parser.add_argument(
    #   'assignee_id', type=int, action='append',
    #   location='args', help='user_id of assignee'
    # )
    # task_parser.add_argument(
    #   'description', type=str, action='append',
    #   location='args', help='task description'
    # )
    # task_parser.add_argument(
    #   'due_date', type=lambda x: datetime.strptime(
    #     x,
    #     "%d/%m/%Y,%H:%M:%S"
    #   ), action='append',
    #   location='args', help='When the required item is due'
    # )
    args = task_parser.parse_args()
    return task_tuple_to_object(delete_task(args['id'][0]))