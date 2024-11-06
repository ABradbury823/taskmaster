from ..swen610_db_utils import *

from .session_utils import generate_sequence_key, hash_string

def create_session(user_id, expires_at = 'infinity'):
  """
  Start a new session for the provided user.

  Parameters:
    user_id (int) - The id of the user.
    expires_at (str) - When the session id expires. Never expires if date is not provided.

  Returns:
    session_id (str) - A hexidecimal code associated with this session.
  """

  # make a new key
  session_key = generate_sequence_key()

  # make a session id by hashing the session key 
  session_id = hash_string(session_key)

  # create session in db
  query = """
  INSERT INTO test.sessions (id, user_id, session_key, created_at, expires_at)
  VALUES(%s, %s, %s, 'now', %s)
  RETURNING *;
  """

  params = (session_id, user_id, session_key, expires_at)

  result = exec_commit_return(query, params)

  return session_id