from ..swen610_db_utils import exec_get_one, exec_get_all

def get_task(task_id:int):
  return exec_get_one("""
      SELECT * FROM test.tasks
      WHERE id = %s;
    """, [task_id])

def get_all_tasks():
  return exec_get_all("""
    SELECT * FROM test.tasks;
  """)