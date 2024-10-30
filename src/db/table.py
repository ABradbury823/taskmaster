class Table():
  def __init__(
      self, name: str, columns: list, 
      # Typing this accurately results in circular import
      database: 'Database' # type: ignore
  ):
    self._name = name
    self._columns = columns
    self._database = database

  def select(self, fields={}, where={}):
    for column in self._columns:
      print(column['column_name'], column['type'], column['nullable'])
    query = f"""
      SELECT *
      FROM {self._name};
    """
    return self._database.select(query)