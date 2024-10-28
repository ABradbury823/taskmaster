import unittest
from src.db.data import create_test_data
from src.db.swen610_db_utils import *
from src.db.users.get_user import *

class TestGetUser(unittest.TestCase):
  def setUp(self):
    create_test_data()

  def test_get_all_users(self):
    """Get all users returns a list of all users"""
    result = get_all_users()
    userCount = exec_get_one('SELECT COUNT(id) from test.users;')[0]
    self.assertEqual(len(result), userCount, "Expected a list of users equal in length to users table.")

  def test_get_user(self):
    """Gets a specific user at a valid id"""
    result = get_user(1)
    user = exec_get_one('SELECT * FROM test.users WHERE id = %s', (1,))
    self.assertEqual(result, user, "Expected information with the id 1.")

  def test_get_invalid_user(self):
    """Returns None if the user id does not match a user"""
    result = get_user(-10)
    self.assertIsNone(result, "Expected output of None when getting user with the id -10.")