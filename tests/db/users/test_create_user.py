import unittest
from src.db.users.create_user import *
from src.db.swen610_db_utils import *

class TestCreateUser(unittest.TestCase):
  def setUp(self):
    exec_sql_file('src/db/create_test_data.sql')

  def test_create_user(self):
    """A new user is created with information in each of it's fields"""
    result = create_user('USER1', 'user1@email.com', 'user1password', 'New User', 'I am new here!')
    user = exec_get_one("SELECT * FROM test.users ORDER BY id DESC LIMIT 1;")
    self.assertEqual(result, user, "Expected to find data on a newly created user.")

  def test_create_user_optionals_empty(self):
    """A new user created with optional parameters left empty will have 
    a matching name and display_name and it's bio will be an empty string"""
    result = create_user('USER1', 'user1@email.com', 'user1password')
    self.assertEqual(result[4], result[1], "Expected new user's name and display_name to match.")
    self.assertEqual(result[5], '', "Expected new user's bio to be an empty string.")

  def test_create_user_optionals_none(self):
    """A new user created with optional parameters set to None will have 
    a matching name and display_name and it's bio will be an empty string"""
    result = create_user('USER1', 'user1@email.com', 'user1password', None, None)
    self.assertEqual(result[4], result[1], "Expected new user's name and display_name to match.")
    self.assertEqual(result[5], '', "Expected new user's bio to be an empty string.")

  #TODO: Test creating a user with name/email already in use, test hash password.