from ..swen610_db_utils import exec_commit_return

def update_task(task_id: int, args={}):
  """
  Update a task in the database
  based on the given id.

  Parameters:
    task_id (int):
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

  columns = []
  values = []

  for col in col_heads:
    if col in args:
      columns.append(f'{col}=%s')
      values.append(args[col])

  if len(values) == 0:
    return None

  values.append(task_id)

  query = f"""
    UPDATE test.tasks
    SET {', '.join(columns)}
    WHERE id = %s
    RETURNING *;
  """
  return exec_commit_return(query, values)
