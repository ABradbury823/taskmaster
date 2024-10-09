from src.db.swen610_db_utils import *

def get_all_users():
  """
  Retrieves information on all users.

  Returns:
    users_list (list[tuple]) - Information on every user in the database in the format
    (user_id, account_name, email, password, display_name, bio)
  """

  query = 'SELECT * FROM tests.users;'

  result = exec_get_all(query)
  return result

def get_user(user_id: int):
  """
  Retrieves information on a specific user.

  Parameters:
    user_id (int) - The user's id.

  Returns:
    user_info (tuple) - Information on the specific user in the format
    (user_id, account_name, email, password, display_name, bio)
  """

  query = 'SELECT * FROM tests.users WHERE id = %s;'

  params = (user_id,)

  result = exec_get_one(query, params)
  return result