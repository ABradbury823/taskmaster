import unittest

from ..test_req_utils import *
from src.db.data import create_test_data
from src.db.users.create_user import create_user

base_url = 'http://localhost:4500'
endpoint = '/login'

# TODO: validate user creds for viewing, updating, and deleting user

class TestLogin(unittest.TestCase):
  def setUp(self):
    create_test_data()
    self.user_creds = ['newuser', 'newuser@email.com', 'newuserpassword']
    create_user(self.user_creds[0], self.user_creds[1], self.user_creds[2])

  def test_get_returns_405_error(self):
    """Get requests are not allowed at login endpoint"""
    test_get(self, base_url + endpoint, expected_status=405)

  def test_post_returns_session_id(self):
    """Post requests return a session id"""
    json = {'username': self.user_creds[0], 'password': self.user_creds[2]}
    result = test_post(self, base_url + endpoint, json=json)
    self.assertTrue('session_id' in result, 'Expected to find a session id on a valid login.')

  def test_post_bad_creds_deny_access(self):
    """Post requests deny access to invalid credentials"""
    json = {'username': 'totally a user', 'password': 'a very real password'}
    result = test_post(self, base_url + endpoint, json=json)
    self.assertFalse('session_id' in result, 'Expected to find a session id on a valid login.')

  def test_put_returns_405_error(self):
    """Get requests are not allowed at login endpoint"""
    test_put(self, base_url + endpoint, expected_status=405)

  def test_delete_returns_405_error(self):
    """Delete requests are not allowed at login endpoint"""
    test_delete(self, base_url + endpoint, expected_status=405)
