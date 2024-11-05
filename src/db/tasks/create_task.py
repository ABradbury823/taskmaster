from ..swen610_db_utils import exec_commit_return

def create_task(taskboard_id:int, args:dict={}):
  """
  Create a new task and add to the database
  in the given taskboard (by id).

  Parameters:
    taskboard_id (int):
    args (dict): Column-value pairs

  Returns:
    new_task (tuple): `(
      id: int, taskboard_id: int
      assignee_id: int | None, name: str,
      description: str, due_date: Datetime | None
    )`
  """
  col_heads = [ 
    'assignee_id', 'name', 'description', 'due_date' 
  ]

  columns = [ 'taskboard_id' ]
  values = [ taskboard_id ]
  replace_str_sequence = ['%s']

  for col in col_heads:
    if col in args:
      columns.append(col)
      values.append(args[col])
      replace_str_sequence.append('%s')

  query = f"""
    INSERT INTO test.tasks
    ({', '.join(columns)})
    VALUES
    ({', '.join(replace_str_sequence)})
    RETURNING *;
  """
  return exec_commit_return(query, values)
