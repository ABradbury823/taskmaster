class Table():
  def __init__(
    self, name: str, columns: list, 
    # Typing this accurately results in circular import
    database: 'Database' # type: ignore
  ):
    self._name = name
    self._columns = columns
    self._database = database

  def select(self, fields:list=[], where:dict={}):
    filtered_fields = []
    filtered_where = []
    values = []
    
    for column in self._columns:
      if column['column_name'] in fields:
        filtered_fields.append(column['column_name'])
      if column['column_name'] in where:
        filtered_where.append(column['column_name'] + '=%s')
        # TODO: validate type
        values.append(where[column['column_name']])

    query = f"""
      SELECT {
        '*' if len(filtered_fields) == 0
        else ', '.join(filtered_fields)
      }
      FROM {self._name}
      {
        '' if len(filtered_where) == 0
        else 'WHERE ' + ' AND '.join(filtered_where)
       };
    """
    return self._database.select(query, values)
  
  def insert(self, fields:dict={}, returning:list=''):
    filtered_fields = []
    value_holder = []
    filtered_returning = []
    values = []

    for column in self._columns:
      if column['column_name'] in fields:
        filtered_fields.append(column['column_name'])
        value_holder.append('%s');
        values.append(fields[column['column_name']])
      if type(returning) is list and column['column_name'] in returning:
        filtered_returning.append(column['column_name'])

    query = f"""
      INSERT INTO {self._name}
      ({', '.join(filtered_fields)})
      VALUES ({', '.join(value_holder)})
      {
        'RETURNING ' + 
        ', '.join(filtered_returning) if type(returning) is list
        else returning
      };
    """
    return self._database.exec_commit(query, values)