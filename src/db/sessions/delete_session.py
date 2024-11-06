from ..swen610_db_utils import *

def delete_session(session_id: int):
  """
  Ends a session.

  Parameters:
    session_id (int) - The session id.

  """
  query = """
  DELETE FROM test.sessions WHERE id LIKE %s;
  """

  params = (session_id,)

  exec_commit(query, params)

