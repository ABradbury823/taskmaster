from .swen610_db_utils import exec_get_one

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