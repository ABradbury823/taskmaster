from ..swen610_db_utils import *
from .session_utils import hash_string
from datetime import datetime

class SessionExpiredError(Exception):
  """
  Exception raised when a session has expired.
  
  Attributes:
    message (str) - explanation of the error
    error_code (int) - the error's status code
  """

  def __init__(self, message, error_code = 403):
    self.message = message
    self.error_code = error_code
    super().__init__(message, error_code)

  def __str__(self):
    return f'{self.message} (Error Code: {self.error_code})'
  

def get_session(session_id: str, check_time: str = 'now'):
  """
  Retrieve a user by session id to check that they are logged in.

  Parameters:
    session_id (str) - The user's session id.
    check_time (str) - The time the session is checked. Defaults to current time.

  Returns:
    session_info (tuple) - Information on the session in the format (user_id, expires_at)
      user_id (int) - The id of the user. 
      expires_at (datetime) - The timestamp when the session expires.
    Returns None if the session id is invalid.
  
  Raises:
    SessionExpiredError - The provided session id has expired.
  """

  query = """
  SELECT user_id, expires_at FROM test.sessions 
  WHERE id LIKE %s;
  """

  params = (session_id,)

  result = exec_get_one(query, params)

  if result is None:
    return None
  
  # session has expired
  expire_at = result[1]
  # this is purely for tests - a custom 'current time'
  cur_time = datetime.now() if check_time == 'now' else datetime.strptime(check_time, '%Y/%m/%d')
  if expire_at < cur_time:
    raise SessionExpiredError(f'The session for this user has expired.')

  return result

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
