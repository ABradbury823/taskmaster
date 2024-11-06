from ..swen610_db_utils import exec_commit_return

def delete_task(task_id: int, args={}):
  """
  Delete a task in the database
  based on the given id.

  Parameters:
    task_id (int):
    args (dict): Column-value pairs

  Returns:
    deleted_task (tuple): `(
      id: int, taskboard_id: int
      assignee_id: int | None, name: str,
      description: str, due_date: Datetime | None
    )`
  """
  # TODO: additional where clauses
  # col_heads = [ 
  #   'assigne_id', 'name', 'description', 'due_date' 
  # ]

  # columns = []
  values = []

  # for col in col_heads:
  #   if col in args:
  #     columns.append(f'{col}=%s')
  #     values.append(args[col])

  # if len(values) == 0:
  #   return None

  values.append(task_id)

  query = f"""
    DELETE FROM test.tasks
    WHERE id = %s
    RETURNING *;
  """
  return exec_commit_return(query, values)
