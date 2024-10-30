class Table():
  def __init__(
      self, name: str, columns: list, 
      # Typing this accurately results in circular import
      database: 'Database' # type: ignore
  ):
    self._name = name
    self._columns = columns
    self._database = database

  def select(self, fields:list=[], where={}):
    filtered_fields = []
    
    for column in self._columns:
      if column['column_name'] in fields:
        filtered_fields.append(column['column_name'])

    query = f"""
      SELECT {
        '*' if len(filtered_fields) == 0
        else ', '.join(filtered_fields)
      }
      FROM {self._name};
    """
    return self._database.select(query)