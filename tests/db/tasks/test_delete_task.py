from unittest import TestCase
from src.db.tasks.delete_task import delete_task
from src.db.swen610_db_utils import (
  exec_sql_file, exec_get_one, exec_get_all
)

class TestDeleteTask(TestCase):
  def setUp(self):
    exec_sql_file('src/db/create_test_data.sql')

  def test_delete_task(self):
    """Task and referencing rows are deleted"""
    original_task = exec_get_one("""
      SELECT * FROM test.tasks
      WHERE id = (
        SELECT MAX(id) from test.tasks
      );
    """)
    categories = exec_get_all("""
      SELECT * FROM test.task_categories
      WHERE task_id = %s;
    """, [original_task[0]])
    self.assertNotEqual(len(categories), 0,
                        'Expected task categoried')
    deleted = delete_task(original_task[0])
    self.assertEqual(
      original_task, 
      deleted,
      'Expected deleted task to be returned'
    )
    self.assertEqual(
      exec_get_one("""
        SELECT * FROM test.tasks
        WHERE id = %s
      """, [original_task[0]]), None,
      'Expected task to be deleted from db'
    )
    deleted_categories = exec_get_all("""
      SELECT * FROM test.task_categories
      WHERE task_id = %s;
    """, [original_task[0]])
    self.assertEqual(
      len(deleted_categories), 0,
      'Expected task categoried'
    )
