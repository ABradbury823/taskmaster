import unittest

from ..test_req_utils import test_get, test_post, test_put, test_delete
from src.db.swen610_db_utils import exec_sql_file, exec_get_one
from datetime import datetime

base_url = 'http://localhost:4500'
endpoint = '/tasks'

class TestTasks(unittest.TestCase):
  def setUp(self):
    exec_sql_file('src/db/create_test_data.sql')

  def test_get_returns_all_tasks(self):
    """Get requests retrieve all tasks in database"""
    results = test_get(self, base_url + endpoint)
    self.assertEqual(5, len(results))

  def test_post_creates_task(self):
    """Post requests return newly-created tasks"""
    task = {
      'taskboard_id': 2,
      'assignee_id': 2,
      'name': 'Find a reason',
      'description': 'Why are we here? Just to suffer?',
      'due_date': datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+"Z"
    }
    res = test_post(self, base_url + endpoint, json=task, expected_status=200)
    for key in task:
      self.assertEqual(
        task[key], res[key], 
        f'Expected {key} to be {task[key]}'
      )

  def test_put_returns_405_error(self):
    """Put requests are not allowed at root endpoint"""
    test_put(self, base_url + endpoint, expected_status=405)

  def test_delete_returns_deleted_from_id(self):
    """Delete requests return deleted item(s)"""
    id = 1
    deleted = list(exec_get_one("SELECT * FROM test.tasks WHERE id=%s;", [id]))
    deleted[5] =  deleted[5].strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+"Z" # due date
    res = test_delete(self, base_url + endpoint + '?id={}'.format(id))
    self.assertEqual(deleted, list(res.values()))

if __name__ == '__main__':
  unittest.main()