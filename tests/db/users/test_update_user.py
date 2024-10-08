import unittest
from src.db.data import create_test_data
from src.db.users.update_user import *
from src.db.swen610_db_utils import *

class TestUpdateUser(unittest.TestCase):
  def setUp(self):
    create_test_data()

  def test_update_user_name(self):
    """Updates a user with a new account name"""
    user_id = 1
    result = update_user_name(user_id, 'BigGuy001')
    user = exec_get_one('SELECT * FROM test.users WHERE id = %s', (user_id,))
    self.assertEqual(result, user, 'Expected user entry and update results to match.')

  # def test_update_user_email(self):
  #   user_id = 