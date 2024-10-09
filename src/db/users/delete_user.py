from src.db.swen610_db_utils import *

def delete_user(user_id: int):
  """
    Deletes a specific user from the database.

    Parameters:
      user_id (int) - The user's id.

    Returns:
      user_info (tuple) - Information on the user that was just deleted in the format
      (user_id, account_name, email, password, display_name, bio)
  """
  #TODO: deleting the last admin on a team?
  query = 'DELETE FROM test.users WHERE id = %s RETURNING *;'

  params = (user_id,)
  
  result = exec_commit_return(query, params)
  return result