from src.db.swen610_db_utils import exec_get_one

def get_task(task_id:int):
  return exec_get_one("""
      SELECT * FROM test.tasks
      WHERE id = %s;
    """, [task_id])