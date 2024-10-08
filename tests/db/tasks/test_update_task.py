from unittest import TestCase
from datetime import datetime

from src.db.swen610_db_utils import (
  exec_sql_file, exec_get_one
)
from src.db.tasks.update_task import update_task

class TestUpdateTask(TestCase):
  def setUp(self):
    exec_sql_file('src/db/create_test_data.sql')
  
  def test_update_task(self):
    """Function updates task attributes"""
    updated_task = list(exec_get_one(
      """SELECT * FROM test.tasks
      WHERE id = (SELECT MAX(id) FROM test.tasks);"""
    ))
    updated_task[3] = 'New name'
    updated_task[4] = 'New description'
    updated_task[5] = datetime.now()
    updated_id = updated_task[0]
    updated_args = {
      'name': updated_task[3],
      'description': updated_task[4],
      'due_date': updated_task[5]
    }
    result = update_task(updated_id, updated_args)
    self.assertEqual(tuple(updated_task), result, 
                     'Expected task to be updated')
    self.assertEqual(result, exec_get_one("""
        SELECT * FROM test.tasks WHERE id = %s;
      """, [updated_id]), 
      'Expected changes to be committed'
    )

  def test_no_args_returns_None(self):
    """Function returns None with no attributes"""
    task_query = """
      SELECT * FROM test.tasks
      WHERE id = (SELECT MAX(id) FROM test.tasks);
    """
    original_task = exec_get_one(task_query)
    self.assertEqual(
      update_task(original_task[0]), None, 
      'Expected update to return None'
    )
    self.assertEqual(
      original_task, exec_get_one(task_query),
      'Expected no change in database'
    )

  def test_invalid_columns_returns_None(self):
    """Function returns None with no attributes"""
    task_query = """
      SELECT * FROM test.tasks
      WHERE id = (SELECT MAX(id) FROM test.tasks);
    """
    original_task = exec_get_one(task_query)
    self.assertEqual(
      update_task(1, { 'key': 'wrong' }), None,
      'Expected Update to return None'
    )
    self.assertEqual(
      original_task, exec_get_one(task_query),
      'Expected no change in database'
    )

  # TODO: errors for bad types
