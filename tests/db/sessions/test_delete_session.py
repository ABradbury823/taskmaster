import unittest

from src.db.data import create_test_data
from src.db.sessions.create_session import *
from src.db.sessions.delete_session import *

class TestDeleteSession(unittest.TestCase):
  def setUp(self):
    create_test_data()
    self.session_id = create_session(1)

  def test_delete_session(self):
    """Deleting a session removes it from the database"""
    delete_session(self.session_id)
    s_id = exec_get_one('SELECT id FROM test.sessions WHERE id LIKE %s', (self.session_id,))
    self.assertIsNone(s_id, "Expected None when selecting a deleted session.")

  def test_delete_bad_session(self):
    """Deleting does nothing on bad session id"""
    len_before = exec_get_all('SELECT COUNT(*) FROM test.sessions;')[0]
    delete_session('I made up a session id!')
    len_after = exec_get_all('SELECT COUNT(*) FROM test.sessions;')[0]
    self.assertEqual(len_before, len_after, "Unexpected difference of sessions when deleting a non-existant session.")
    
