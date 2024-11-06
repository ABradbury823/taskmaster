import unittest

from ..test_req_utils import test_get, test_post, test_put, test_delete
from src.db.swen610_db_utils import exec_sql_file, exec_get_all
from src.db.sessions.session_utils import hash_string

base_url = 'http://localhost:4500'
endpoint = '/users'

class TestUsers(unittest.TestCase):
  def setUp(self):
    exec_sql_file('src/db/create_test_data.sql')

  def test_get_all_users(self):
    """Get requests retrieve data on all users"""
    result = test_get(self, base_url + endpoint)
    users = exec_get_all('SELECT * FROM test.users')
    self.assertEqual(result['count'], len(users), 'Unexpected total number of users.')
  
  def test_post_new_user(self):
    """Post requests return data on a new user"""
    new_user = {
      'name': 'new_user',
      'email': 'newuser@email.com',
      'password': 'newpassword',
      'display_name': 'New User',
      'bio': 'This is a new user'
    }
    result = test_post(self, base_url + endpoint, json=new_user)
    new_user.pop('password')
    self.assertDictEqual(new_user, result, "Unexpected data for newly-created user.")

  def test_post_required_fields_only(self):
    """Post requests provide default values for optional fields"""
    new_user = {
      'name': 'new_user',
      'email': 'newuser@email.com',
      'password': 'newpassword'
    }
    result = test_post(self, base_url + endpoint, json=new_user)
    new_user['display_name'] = new_user['name']
    new_user['bio'] = ''
    new_user.pop('password')
    self.assertDictEqual(new_user, result, "Unexpected data for newly-created user.")

  def test_post_extra_args(self):
    """Post requests with extra arguments are not allowed"""
    new_user = {
      'name': 'new_user',
      'personality': 'the coolest guy here',
      'email': 'newuser@email.com',
      'password': 'newpassword',
      'coolness': 10000
    }
    result = test_post(self, base_url + endpoint, json=new_user, expected_status=400)

  def test_post_missing_req_args(self):
    """Post requests with missing required arguments are not allowed"""
    new_user = {
      'name': 'new_user',
      'display_name': 'Password-less User',
      'bio': 'Who needs emails and passwords anyway?'
    }
    result = test_post(self, base_url + endpoint, json=new_user, expected_status=400)

  def test_put_returns_405_error(self):
    """Put requests are not allowed at users endpoint"""
    test_put(self, base_url + endpoint, expected_status=405)

  def test_delete_returns_405_error(self):
    """Delete requests are not allowed at users endpoint"""
    test_delete(self, base_url + endpoint, expected_status=405)



