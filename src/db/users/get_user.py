from ..swen610_db_utils import *

def get_all_users():
  """
  Retrieves information on all users.

  Returns:
    users_list (list[tuple]) - Information on every user in the database in the format
    (user_id, account_name, email, password, display_name, bio).
    Results are ordered by id.
  """

  query = 'SELECT * FROM test.users ORDER BY id;'

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

  query = 'SELECT * FROM test.users WHERE id = %s;'

  params = (user_id,)

  result = exec_get_one(query, params)
  return result

def get_user_by_name(user_name: str):
  """
  Retrieves information on a specific user.

  Parameters:
    user_name (str) - The user's account name (case-agnostic).

  Returns:
    user_info (tuple) - Information on the specific user in the format
    (user_id, account_name, email, password, display_name, bio)
  """

  query = 'SELECT * FROM test.users WHERE LOWER(name) LIKE LOWER(%s)'

  params = (user_name,)

  result = exec_get_one(query, params)
  return result

def is_user_name_used(user_name: str):
  """
  Determines if a username is already attached to a user.

  Parameters:
    user_name (str) - The account name (case-agnostic).

  Returns:
    True if a user with the given username exists. False if they do not.
  """
  return (get_user_by_name(user_name) is not None)

def get_user_by_email(user_email: str):
  """
  Retrieves information on a specific user.

  Parameters:
    user_email (str) - The user's email (case-agnostic).

  Returns:
    user_info (tuple) - Information on the specific user in the format
    (user_id, account_name, email, password, display_name, bio)
  """

  query = 'SELECT * FROM test.users WHERE LOWER(email) LIKE LOWER(%s)'

  params = (user_email,)

  result = exec_get_one(query, params)
  return result

def is_user_email_used(user_email: str):
  """
  Determines if an email is already attached to a user.

  Parameters:
    user_email (str) - The account email (case-agnostic).

  Returns:
    True if a user with the given email exists. False if they do not.
  """
  return (get_user_by_email(user_email) is not None)

