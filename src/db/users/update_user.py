from src.db.swen610_db_utils import *

def build_update_user_query(user_id: int, args: dict[str] = {}):
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
  
  query = f"""
  UPDATE test.users 
  SET {', '.join(columns)}
  WHERE id = %s
  RETURNING *;
  """

  return (query, params)



def update_user_name(user_id: int, new_name: str):

  query, params = build_update_user_query(user_id, {'name': new_name})

  result = exec_commit_return(query, params)
  return result



