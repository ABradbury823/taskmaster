from unittest import TestCase
from src.db.swen610_db_utils import (
  exec_sql_file, exec_get_one
)
from src.db.tasks.get_task import get_task

class TestGetTask(TestCase):
  def setUp(self):
    exec_sql_file('src/db/create_test_data.sql')

  def test_get_task(self):
    """Function retrieves task"""
    task = exec_get_one("""
        SELECT * FROM test.tasks
        WHERE id = (
          SELECT MAX(id) FROM test.tasks
        );
      """)
    id = task[0]
    self.assertEqual(
      task, get_task(id),
      'Expected to retrieve task from db'
    )

  def test_get_task_with_invalid_id(self):
    """Function returns None on invalid ids"""
    id = -1
    self.assertEqual(
      None, get_task(id),
      'Expected bad id to return None'
    )