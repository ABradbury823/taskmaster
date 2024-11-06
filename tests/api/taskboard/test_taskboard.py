import unittest

from ..test_req_utils import test_get, test_post, test_put, test_delete
from src.db.swen610_db_utils import exec_get_one, exec_sql_file

base_url = 'http://localhost:4500'
endpoint = '/taskboards/{}'

class TestTaskboard(unittest.TestCase):
  def setUp(self):
    exec_sql_file('src/db/create_test_data.sql')

  def test_get_returns_specific_taskboard(self):
    """taskboards endpoint should return specified taskboard"""
    id = 1
    entity = exec_get_one("SELECT * FROM test.taskboards WHERE id=%s;", [id])
    taskboard_obj = {
      'id': entity[0],
      'team_id': entity[1],
      'name': entity[2],
    }
    taskboard = test_get(self, base_url + endpoint.format(id))
    self.assertEqual(taskboard, taskboard_obj, 'Expected taskboard to be returned')

  def test_post_returns_405_error(self):
    """Post requests are not allowed at root endpoint"""
    id = 1
    test_post(self, base_url + endpoint.format(id), expected_status=405)

  def test_put_returns_405_error(self):
    """Put requests are not allowed at root endpoint"""
    id = 1
    test_put(self, base_url + endpoint.format(id), expected_status=405)

  def test_delete_returns_405_error(self):
    """Delete requests are not allowed at root endpoint"""
    id = 1
    test_delete(self, base_url + endpoint.format(id), expected_status=405)

if __name__ == '__main__':
  unittest.main()