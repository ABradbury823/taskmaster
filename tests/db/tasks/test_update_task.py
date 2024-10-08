from unittest import TestCase

from src.db.swen610_db_utils import (
  exec_sql_file, exec_get_one
)
from src.db.tasks.update_task import update_task

class TestUpdateTask(TestCase):
  def setUp(self):
    exec_sql_file('src/db/create_test_data.sql')
  
  def test_update_task(self):
    updated_task = list(exec_get_one(
      """SELECT * FROM test.tasks
      WHERE id = (SELECT MAX(id) FROM test.tasks);"""
    ))
    updated_task[3] = 'New name'
    updated_task[4] = 'New description'
    updated_id = updated_task[0]
    updated_args = {
      'name': updated_task[3],
      'description': updated_task[4]
    }
    result = update_task(updated_id, updated_args)
    self.assertEqual(tuple(updated_task), result, 
                     'Expected task to be updated')