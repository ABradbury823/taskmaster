import unittest

from ..test_req_utils import *
from src.db.data import create_test_data
from src.db.sessions.create_session import create_session
from src.db.users.create_user import create_user

base_url = 'http://localhost:4500'

class TestLogout(unittest.TestCase):
  def setUp(self):
    create_test_data()
    self.user_creds = ['newuser', 'newuser@email.com', 'newuserpassword']
    self.u_id = create_user(self.user_creds[0], self.user_creds[1], self.user_creds[2])[0]
    self.session_id = create_session(self.u_id)
    self.endpoint = '/logout/' + str(self.u_id)

  def test_get_returns_405_error(self):
    """Get requests are not allowed at login endpoint"""
    test_get(self, base_url + self.endpoint, expected_status=405)

  def test_post_returns_200(self):
    """Post requests return a successful status code"""
    header = {'session-id': self.session_id}
    test_post(self, base_url + self.endpoint, header=header, expected_status=200)

  def test_post_no_session_returns_400_error(self):
    """Post requests without session ids are bad requests"""
    test_post(self, base_url + self.endpoint, expected_status=400)

  def test_post_logout_twice_returns_401(self):
    """Post requests from logged-out users are denied"""
    header = {'session-id': self.session_id}
    test_post(self, base_url + self.endpoint, header=header, expected_status=200)
    test_post(self, base_url + self.endpoint, header=header, expected_status=401)

  def test_post_bad_session_returns_401(self):
    """Post requests deny access to invalid session ids"""
    header = {'session-id': 'I made up this session id'}
    test_post(self, base_url + self.endpoint, header=header, expected_status=401)

  def test_post_bad_user_returns_401(self):
    """Post requests deny access to invalid user ids"""
    header = {'session-id': self.session_id}
    test_post(self, base_url + '/logout/100', header=header, expected_status=401)

  def test_put_returns_405_error(self):
    """Get requests are not allowed at login endpoint"""
    test_put(self, base_url + self.endpoint, expected_status=405)

  def test_delete_returns_405_error(self):
    """Delete requests are not allowed at login endpoint"""
    test_delete(self, base_url + self.endpoint, expected_status=405)