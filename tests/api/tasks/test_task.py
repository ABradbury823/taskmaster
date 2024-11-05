import unittest

from ..test_req_utils import test_get, test_post, test_put, test_delete
from src.db.swen610_db_utils import exec_sql_file, exec_get_one

base_url = 'http://localhost:4500'
endpoint = '/tasks'

class TestTask(unittest.TestCase):
  def setUp(self):
    exec_sql_file('src/db/create_test_data.sql')

  def test_get_id_returns_task(self):
    """Get request of valid id retrieves task from database"""
    id = 1
    task = exec_get_one("SELECT * FROM test.tasks WHERE id=%s;", [id])
    task_obj = {
      'id': task[0],
      'taskboard_id': task[1],
      'assignee_id': task[2],
      'name': task[3],
      'description': task[4],
      'due_date': task[5].strftime("%d/%m/%Y,%H:%M:%S"),

    }
    result = test_get(self, base_url + endpoint + '/{}'.format(id))
    self.assertEqual(task_obj, result)

  def test_post_returns_405_error(self):
    """Post requests are not allowed at specific task endpoint"""
    test_post(self, base_url + endpoint + '/1', expected_status=405)

  def test_put_returns_405_error(self):
    """Put requests are not allowed at root endpoint"""
    test_put(self, base_url + endpoint + '/1', expected_status=405)

  def test_delete_returns_deleted_from_id(self):
    """Delete requests return deleted task"""
    id = 1
    deleted = list(exec_get_one("SELECT * FROM test.tasks WHERE id=%s;", [id]))
    deleted[5] =  deleted[5].strftime("%d/%m/%Y,%H:%M:%S") # due date
    res = test_delete(self, base_url + endpoint + '?id={}'.format(id))
    self.assertEqual(deleted, list(res.values()))

  def test_delete_removes_task_from_database(self):
    """Delete requests delete the task"""
    id = 1
    test_delete(self, base_url + endpoint + '?id={}'.format(id))
    deleted = exec_get_one("SELECT * FROM test.tasks WHERE id=%s;", [id])
    self.assertIsNone(deleted)

if __name__ == '__main__':
  unittest.main()