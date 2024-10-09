import unittest
from src.db.data import create_test_data
from src.db.swen610_db_utils import *
from src.db.users.delete_user import *
from src.db.users.get_user import *

class TestDeleteUser(unittest.TestCase):
  def setUp(self):
    create_test_data()

  def test_delete_user(self):
    """Deleting a user removes them from the db"""
    result = delete_user(2)
    user = get_user(2)
    self.assertIsNone(user, f'Expected no data for user with the id 2 after deletion.')

  def test_delete_user_deletes_team(self):
    """Deleting a user removes their team member entries"""
    result = delete_user(2)
    member_of_teams = exec_get_all('SELECT * FROM test.team_members WHERE user_id = %s', (2,))
    self.assertEqual(member_of_teams, [], 'Expected deleted user to not be present in any teams.')

  def test_delete_user_nulls_assignee(self):
    """Deleting a user nulls assignee id of their tasks"""
    result = delete_user(2)
    # user 2 (Adam) was assigned to task 1
    task = exec_get_one('SELECT * FROM test.tasks WHERE id = %s', (1,))
    self.assertIsNone(task[2], 'Expected task assignee to be null after user deletion.')