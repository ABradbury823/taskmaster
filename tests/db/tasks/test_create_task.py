import unittest

from src.db.tasks.create_task import create_task
from src.db.swen610_db_utils import exec_get_one, exec_sql_file

class TestCreateTask(unittest.TestCase):
  def setUp(self):
    exec_sql_file('src/db/create_test_data.sql')

  def test_create_task(self):
    max_task_id = exec_get_one("SELECT MAX(id) FROM test.tasks;")[0]
    taskboard_id = exec_get_one("SELECT MAX(id) FROM test.taskboards;")[0]
    task_attrs = { 
      'name': 'Create a reason',
      'description': 'Testing'
    }
    new_task = create_task(taskboard_id, task_attrs)
    self.assertEqual(new_task[0], max_task_id + 1,
                     'Expected id to increment max')
    self.assertEqual(new_task[1], taskboard_id,
                     'Expected taskboard_id to match')
    self.assertEqual(new_task[2], None,
                     'Expected assignee_id to be None')
    self.assertEqual(new_task[3], task_attrs['name'],
                     'Expected name to match task arg')
    self.assertEqual(new_task[4], task_attrs['description'],
                     'Expected description to match task arg')
    self.assertEqual(new_task[5], None,
                     'Expected due_date to be None')
