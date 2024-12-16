import unittest

from src.db.sessions.create_session import create_session
from src.db.users.create_user import create_user

from ..test_req_utils import test_get, test_post, test_put, test_delete
from src.db.swen610_db_utils import exec_sql_file, exec_get_one

class TestUser(unittest.TestCase):
  def setUp(self):
    exec_sql_file('src/db/create_test_data.sql')
    self.user_info = ['newuser', 'newuser@email.com', 'newuserpassword']
    self.u_id = create_user(self.user_info[0], self.user_info[1], self.user_info[2])[0]
    self.session_id = create_session(self.u_id)[0]
    self.header = {'session-id': self.session_id}
    self.url = 'http://localhost:4500/users/' + str(self.u_id)

  def test_get_returns_user(self):
    """Get requests retrieve a user's data"""
    result = test_get(self, self.url, expected_status=200)
    self.assertGreater(len(result), 0, 'Expected data to be returned from get.')
  
  def test_post_returns_405_error(self):
    """Post requests are not allowed at user endpoint"""
    test_post(self, self.url, expected_status=405)

  def test_put_updates_user(self):
    """Put requests update a user's fields"""
    updated_user = {
      'name': 'big_guy00',
      'email': 'mrG@email.com',
      'password': 'bigGRocks',
      'display_name': 'The Big Guy',
      'bio': 'Just your average user.'
    }
    result = test_put(self, self.url, json=updated_user, header=self.header)
    updated_user.pop('password')
    self.assertDictEqual(updated_user, result, 'Unexpected data when updating a user.')

  def test_put_no_id_returns_400(self):
    """Put requests with no session id are a bad request"""
    updated_user = {
      'name': 'big_guy00',
      'email': 'mrG@email.com',
      'password': 'bigGRocks',
      'display_name': 'The Big Guy',
      'bio': 'Just your average user.'
    }
    test_put(self, self.url, json=updated_user, expected_status=400)

  def test_put_no_session_returns_401(self):
    """Put requests from a logged-out user are unauthorized"""
    test_post(self, f'http://localhost:4500/logout/{self.u_id}', header=self.header)
    updated_user = {
      'name': 'big_guy00',
      'email': 'mrG@email.com',
      'password': 'bigGRocks',
      'display_name': 'The Big Guy',
      'bio': 'Just your average user.'
    }
    test_put(self, self.url, json=updated_user, header=self.header, expected_status=401)

  def test_put_wrong_user_returns_401(self):
    """Put requests from an incorrect user id are unauthorized"""
    updated_user = {
      'name': 'big_guy00',
      'email': 'mrG@email.com',
      'password': 'bigGRocks',
      'display_name': 'The Big Guy',
      'bio': 'Just your average user.'
    }
    test_put(self, f'http://localhost:4500/users/1', json=updated_user, 
             header=self.header, expected_status=401)

  def test_delete_removes_user(self):
    """Delete requests remove a user"""
    test_delete(self, self.url, header=self.header, expected_status=200)
    result = test_get(self, self.url)
    self.assertEqual(len(result), 1, "Found unexpected data for a deleted user.")

  def test_delete_no_id_returns_400(self):
    """Delete requests with no session id are a bad request"""
    test_delete(self, self.url, expected_status=400)
