import unittest

from src.db.data import create_test_data
from src.db.sessions.create_session import *
from src.db.sessions.get_session import *
from src.db.sessions.delete_session import *
from src.db.users.create_user import create_user
from src.db.users.get_user import get_user_by_name

class TestGetSession(unittest.TestCase):
  def setUp(self):
    create_test_data()
    self.user_id = 1
    self.session_id = create_session(self.user_id)[0]

  def test_get_session_logged_in(self):
    """Get session returns logged in user's id"""
    result = get_session(self.session_id)
    self.assertEqual(result[0], self.user_id, 'Unexpected user id for session.')

  def test_get_session_logged_out(self):
    """Get session returns None if the user is not logged in"""
    delete_session(self.session_id)
    result = get_session(self.session_id)
    self.assertIsNone(result, 'Expected None when retrieving a deleted session.')
    
  def test_get_session_expired(self):
    """Get session raises a SessionExpiredError if session has expired"""
    new_session_id = create_session(2, 'tomorrow')[0]
    try: 
      with self.assertRaises(SessionExpiredError):
        get_session(new_session_id, '2100/01/01')
    except AssertionError:
      self.fail("Expected a SessionExpiredError to be raised when getting an expired session.")

  def test_valid_user_creds_id(self):
    """Return user_id if user credentials match"""
    create_user('newuser', 'newuser@email.com', 'newuserpassword')
    user_id = get_user_by_name('newuser')[0]
    result = validate_user_creds('newuser', 'newuserpassword')
    self.assertEqual(result, user_id, 'Expected matching credentials to return the user\'s id.')
  
  def test_valid_user_creds_none(self):
    """Return None if user credentials do not match"""
    result = validate_user_creds('a real user', 'password123')
    self.assertIsNone(result, 'Expected incorrect credentials to return None.')


