from .swen610_db_utils import *
from .sessions.session_utils import hash_string
from .users.update_user import update_user_password

def create_test_data():
  """Builds a test database from a SQL file."""
  exec_sql_file('src/db/create_test_data.sql')

def create_test_data_client():
  """Builds a test database from a SQL file for testing the client application"""
  exec_sql_file('src/db/create_test_data.sql')

  query = """
  SELECT id, password FROM test.users;
  """

  users = exec_get_all(query)

  for user in users :
    update_user_password(user[0], user[1])


def does_data_exist(schema_name: str):
  """
  Checks that a database schema exists.

  Parameters:
    schema_name (str) - Name of the schema.

  Returns: True if the schema is found in the information schema.
    False if the schema does not exist.
  """

  # Check if the schema exists in the information schema
  #  https://www.postgresql.org/docs/current/infoschema-tables.html
  query = """
  SELECT * FROM information_schema.tables
  WHERE table_schema = %s;
  """

  params = (schema_name,)

  result = exec_get_one(query, params)

  # if there is no schema, the result will be None
  return result != None