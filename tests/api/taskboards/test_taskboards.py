import unittest

from ..test_req_utils import test_get, test_post, test_put, test_delete
from src.db.swen610_db_utils import exec_sql_file

base_url = 'http://localhost:4500'
endpoint = '/taskboards'

class TestTaskboards(unittest.TestCase):
  def setUp(self):
    exec_sql_file('src/db/create_test_data.sql')
  
  def test_get_returns_all_taskboards(self):
    """taskboards endpoint should return all taskboards"""
    taskboards = test_get(self, base_url + endpoint)
    self.assertEqual(2, len(taskboards), 'Expected 2 taskboards to be returned')

  def test_post_returns_405_error(self):
    """Post requests are not allowed at taskboards endpoint"""
    test_post(self, base_url, expected_status=405)

  def test_put_returns_405_error(self):
    """Put requests are not allowed at taskboards endpoint"""
    test_put(self, base_url, expected_status=405)

  def test_delete_returns_405_error(self):
    """Delete requests are not allowed at taskboards endpoint"""
    test_delete(self, base_url, expected_status=405)

if __name__ == '__main__':
  unittest.main()