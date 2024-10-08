from src.db.swen610_db_utils import *

def _build_update_user_query(user_id: int, args: dict[str, str]):
  """
  Builds a SQL query for updating the fields of a user.

  Parameters:
    user_id (int) - The user's id.
    args (dict[str, str]) - Key/value arguments representing the column names and new values of user data.

  Returns:
    query_values (tuple) - The formatted query string and the list of value parameters.
  """

  user_cols = [
    'name', 'email', 'password', 'display_name', 'bio'
  ]

  columns = []
  params = []
  for col in user_cols:
    if(col in args):
      columns.append(f'{col} = %s')
      params.append(args[col])

  params.append(user_id)
  
  # QUESTION: do we really want/need to update more than one column at once?
  query = f"""
  UPDATE test.users 
  SET {', '.join(columns)}
  WHERE id = %s
  RETURNING *;
  """

  return (query, params)

def update_user(user_id: int, args: dict[str, str]):
  """
  Updates the user's account information. Multiple values can be changed at once with an argument dictionary.

  Parameters:
    user_id (int) - The user's id.
    args (dict[str]) - Key/value arguments representing column names and their desired values.
    Valid keys include name, email, password, display_name, and bio.
    All values are strings.

  Returns:
    user_info (tuple) - The updated user's information in the format
    (id, name, email, password, display_name, bio).
  """

  query, params = _build_update_user_query(user_id, args)

  result = exec_commit_return(query, params)
  return result

def update_user_name(user_id: int, new_name: str):
  """
  Updates the user's account name.

  Parameters:
    user_id (int) - The user's id.
    new_name (str) - The desired new name.

  Returns:
    user_info (tuple) - The updated user's information in the format
    (id, name, email, password, display_name, bio).
  """

  query, params = _build_update_user_query(user_id, {'name', new_name})

  result = exec_commit_return(query, params)
  return result

def update_user_email(user_id: int, new_email: str):
  """
  Updates the user's account name.

  Parameters:
    user_id (int) - The user's id.
    new_email (str) - The desired new email.

  Returns:
    user_info (tuple) - The updated user's information in the format
    (id, name, email, password, display_name, bio).
  """

  query, params = _build_update_user_query(user_id, {'email', new_email})

  result = exec_commit_return(query, params)
  return result

def update_user_password(user_id: int, new_password: str):
  """
  Updates the user's account password.

  Parameters:
    user_id (int) - The user's id.
    new_password (str) - The desired new password.

  Returns:
    user_info (tuple) - The updated user's information in the format
    (id, name, email, password, display_name, bio).
  """

  query, params = _build_update_user_query(user_id, {'password', new_password})

  result = exec_commit_return(query, params)
  return result

def update_user_display_name(user_id: int, new_display_name: str):
  """
  Updates the user's display name, the name that is shown to other users when viewing 
  this user's account.

  Parameters:
    user_id (int) - The user's id.
    new_display_name (str) - The desired new display name.

  Returns:
    user_info (tuple) - The updated user's information in the format
    (id, name, email, password, display_name, bio).
  """

  query, params = _build_update_user_query(user_id, {'display_name', new_display_name})

  result = exec_commit_return(query, params)
  return result

def update_user_bio(user_id: int, new_bio: str):
  """
  Updates the user's bio, the information shown under the user's 'About Me' section.

  Parameters:
    user_id (int) - The user's id.
    new_bio (str) - The desired new bio.

  Returns:
    user_info (tuple) - The updated user's information in the format
    (id, name, email, password, display_name, bio).
  """

  query, params = _build_update_user_query(user_id, {'bio', new_bio})

  result = exec_commit_return(query, params)
  return result


