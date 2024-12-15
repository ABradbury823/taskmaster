from ..swen610_db_utils import *
from .session_utils import hash_string

def get_session(session_id: str, check_time: str = 'now'):
  """
  Retrieve a user by session id to check that they are logged in.

  Parameters:
    session_id (str) - The user's session id.
    session_id (str) - The time the session is checked. Defaults to current time.

  Returns:
    user_id (int) - The id of the user. 
    Returns None if the session id is invalid or expired.
  """

  query = """
  SELECT user_id FROM test.sessions 
  WHERE id = %s AND (expires_at = 'infinity' OR expires_at > %s);
  """

  params = (session_id, check_time,)

  result = exec_get_one(query, params)

  if result is None:
    return None

  return result[0]

def validate_user_creds(username: str, password: str):
  """
  Checks that the provided credentials belong to a user.

  Parameters:
    username (str) - The user's account name.
    password (str) - The user's password.

  Returns:
    The user's id if the credentials belong to a user. None if they do not.
  """

  password = hash_string(password)
  
  query = """
  SELECT * FROM test.users
  WHERE name LIKE %s AND password LIKE %s;
  """

  params = (username, password,)

  result = exec_get_one(query, params)

  if(result is None):
    return None

  return result[0]
