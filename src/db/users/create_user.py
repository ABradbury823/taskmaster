from src.db.swen610_db_utils import *

def create_user(name: str, email: str, password: str, display_name:str = '', bio: str = ''):
  """
  Creates a new user and adds them to the database.

  Parameters:
    name (str) - The user's account name. Must be unique.
    email (str) - The user's email. Must be unique.
    password (str) - The user's password.
    display_name (str) - The name shown to others when viewing the account (e.g. nickname). 
    Defaults to the user's account name.
    bio (str) - A snippet about the user. Defaults to empty.

  Returns:
    user_info (tuple) - Information about the new user in the format
    (user_id, user_name, email, password, display_name, bio)
  """

  #TODO: Check if user name/email are already in use, hash password.

  # if the display name is empty, set it to the username
  if(display_name == '' or display_name is None): display_name = name

  # probably not needed, but you never know when empty input will send None
  if(bio is None): bio = ''
  
  query = """
  INSERT INTO test.users (name, email, password, display_name, bio)
  VALUES (%s, %s, %s, %s, %s)
  RETURNING *;
  """

  params = (name, email, password, display_name, bio)

  result = exec_commit_return(query, params)
  return result