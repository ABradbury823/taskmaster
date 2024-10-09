import unittest
from src.db.data import create_test_data
from src.db.swen610_db_utils import *
from src.db.users.get_users import *

class TestGetUser(unittest.TestCase):
  def setUp(self):
    create_test_data()

  def test_get_all_users(self):
    """Get all users returns a list of all users"""
    result = get_all_users()
    userCount = exec_get_one('SELECT COUNT(id) from test.users;')[0]
    self.assertEqual(len(result), userCount, "Expected a list of users equal in length to users table.")