import unittest
from src.db.data import create_test_data
from src.db.users.create_user import *
from src.db.swen610_db_utils import *

class TestCreateUser(unittest.TestCase):
  def setUp(self):
    create_test_data()

  def test_create_user(self):
    """Creates a new user with all fields filled"""
    result = create_user('USER1', 'user1@email.com', 'user1password', 'New User', 'I am new here!')
    user = exec_get_one("SELECT * FROM test.users ORDER BY id DESC LIMIT 1;")
    self.assertEqual(result, user, "Expected to find data on a newly created user.")

  def test_create_user_optionals_empty(self):
    """Creates a new user with defaulted display name and bio"""
    result = create_user('USER1', 'user1@email.com', 'user1password')
    self.assertEqual(result[4], result[1], "Expected new user's name and display_name to match.")
    self.assertEqual(result[5], '', "Expected new user's bio to be an empty string.")

  def test_create_user_optionals_none(self):
    """Creates a new user with non-None display name and bio"""
    result = create_user('USER1', 'user1@email.com', 'user1password', None, None)
    self.assertEqual(result[4], result[1], "Expected new user's name and display_name to match.")
    self.assertEqual(result[5], '', "Expected new user's bio to be an empty string.")

  def test_create_user_duplicate_name(self):
    """New user is not made if username is already used"""
    result = create_user('adam', 'adamtheadam@email.com', 'adamspassword')
    self.assertIsNone(result, "Expected no result when making a user with a duplicate name.")

  def test_create_user_duplicate_email(self):
    """New user is not made if email is already used"""
    result = create_user('user1', 'adam@email.com', 'userpassword')
    self.assertIsNone(result, "Expected no result when making a user with a duplicate email.")
  
  def test_user_password_hashed(self):
    """New users have their passwords hashed"""
    result = create_user('USER1', 'user1@email.com', 'user1password', 'New User', 'I am new here!')
    self.assertNotEqual('user1password', result[3], 'Expected password to be hashed when creating a new user.')
  
