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
      'due_date': task[5].strftime("%Y-%m-%dT%H:%M:%S"),

    }
    result = test_get(self, base_url + endpoint + '/{}'.format(id))
    self.assertEqual(task_obj, result)

  def test_post_returns_405_error(self):
    """Post requests are not allowed at specific task endpoint"""
    test_post(self, base_url + endpoint + '/1', expected_status=405)

  def test_put_returns_updated_task(self):
    """Put requests return the updated object"""
    id = 1
    updated = list(exec_get_one("SELECT * FROM test.tasks WHERE id=%s;", [id]))
    updated[3] = 'new name'
    updated[4] = 'new description'
    updated_obj = {
      'id': updated[0],
      'taskboard_id': updated[1],
      'assignee_id': updated[2],
      'name': updated[3],
      'description': updated[4],
      'due_date': updated[5].strftime("%Y-%m-%dT%H:%M:%S"),
    }
    res = test_put(self, base_url + endpoint + '/{}'.format(id), json=updated_obj)
    self.assertEqual(updated_obj, res)

  def test_put_is_updated_in_database(self):
    """Put requests overwrite the object in the database"""
    id = 1
    updated = list(exec_get_one("SELECT * FROM test.tasks WHERE id=%s;", [id]))
    updated[3] = 'new name'
    updated[4] = 'new description'
    updated_obj = {
      'id': updated[0],
      'taskboard_id': updated[1],
      'assignee_id': updated[2],
      'name': updated[3],
      'description': updated[4],
      'due_date': updated[5].strftime("%Y-%m-%dT%H:%M:%S"),
    }
    test_put(self, base_url + endpoint + '/{}'.format(id), json=updated_obj)
    db_task = exec_get_one("SELECT * FROM test.tasks WHERE id=%s;", [id])
    self.assertEqual(updated, list(db_task))

  def test_delete_returns_deleted_from_id(self):
    """Delete requests return deleted task"""
    id = 1
    deleted = list(exec_get_one("SELECT * FROM test.tasks WHERE id=%s;", [id]))
    deleted[5] =  deleted[5].strftime("%Y-%m-%dT%H:%M:%S") # due date
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