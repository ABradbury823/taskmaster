import unittest
from src.db.data import create_test_data
from src.db.swen610_db_utils import *
from src.db.users.update_user import *

class TestUpdateUser(unittest.TestCase):
  def setUp(self):
    create_test_data()

  def get_user(self, user_id: int):
    """
    Retreives a user by id.
    
    Parameters:
      user_id (int) - The user's id.

    Returns:
      user_info (tuple) - The user's information in the format
      (user_id, account_name, email, password, display_name, bio)
    """
    return exec_get_one('SELECT * FROM test.users WHERE id = %s', (user_id,))

  def test_update_user_name(self):
    """Updates a user with a new account name"""
    user_id = 1
    result = update_user_name(user_id, 'BigGuy001')
    user = self.get_user(user_id)
    self.assertEqual(result, user, 'Expected user entry and update results to match.')

  def test_update_user_email(self):
    """Updates a user with a new email"""
    user_id = 1
    result = update_user_email(user_id, 'changed@email.com')
    user = self.get_user(user_id)
    self.assertEqual(result, user, 'Expected user entry and update results to match.')

  def test_update_user_password(self):
    """Updates a user with a new password"""
    user_id = 1
    result = update_user_password(user_id, 's3cur3rp@55w0rd')
    user = self.get_user(user_id)
    self.assertEqual(result, user, 'Expected user entry and update results to match.')

  def test_update_user_display_name(self):
    """Updates a user with a new display name"""
    user_id = 1
    result = update_user_display_name(user_id, 'The Gardener')
    user = self.get_user(user_id)
    self.assertEqual(result, user, 'Expected user entry and update results to match.')

  def test_update_user_bio(self):
    """Updates a user with a new bio"""
    user_id = 1
    result = update_user_bio(user_id, 'On that 7 day grind :muscle:')
    user = self.get_user(user_id)
    self.assertEqual(result, user, 'Expected user entry and update results to match.')

  def test_update_user_all_fields(self):
    """Updates all of a user's fields at once"""
    user_id = 1
    result = update_user(
      user_id, 
      {
        'name': 'BigG007',
        'email': 'bigg@hotmail.com',
        'password': 'bigGuyUpStairs',
        'display_name': 'ComMANdment Giver',
        'bio': 'Still on the grind, not planning on stopping soon :triumph:'
      }
    )
    user = self.get_user(user_id)
    self.assertEqual(result, user, 'Expected user entry and update results to match.')

  def test_update_prune_invalid_fields(self):
    """Invalid fields are not considered in update arguments"""
    user_id = 1
    result = update_user(
      user_id,
      {
        'hello': 3,
        'name': 'New Name',
        'whatever': 'whatevs',
        15: 31
      }
    )
    user = self.get_user(user_id)
    self.assertEqual(len(result), len(user), "Expected same number of columns when invalid fields are provided.")

  def test_update_all_fields_invalid(self):
    """Updating full set of invalid arguments returns None"""
    result = update_user(1, {'coolness': 'yeah', 'awesomeness': 'hell yeah', 'super_password': 'ultrapassword'})
    self.assertIsNone(result, "Expected None when updating a set of invalid user fields.")

  def test_update_duplicate_name(self):
    """User is not updated if username is already used"""
    result = update_user_name(1, 'adam')
    self.assertIsNone(result, "Expected no result when updating a user with a duplicate name")

  def test_update_duplicate_email(self):
    """User is not updated if email is already used"""
    result = update_user_email(1, 'adam@email.com')
    self.assertIsNone(result, "Expected no result when updating a user with a duplicate email")




  

