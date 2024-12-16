import unittest

from src.db.data import create_test_data
from src.db.sessions.create_session import *

class TestCreateSession(unittest.TestCase):
  def setUp(self):
    create_test_data()
  
  def test_create_session(self):
    """Creating a session returns a session id"""
    user_id = 1
    result = create_session(user_id)
    id = exec_get_one('SELECT id FROM test.sessions WHERE user_id = %s;', (user_id,))[0]
    self.assertEqual(id, result[0], "Unexpected session id for new session.")
    
