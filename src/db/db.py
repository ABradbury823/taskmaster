import psycopg2
import yaml
import os.path as path

class Database():
  @staticmethod
  def connect():
    """Connect to the database with data from ~/config/db.yml"""
    # credit swen610_db_utils
    config = {}
    yml_path = path.join(path.dirname(__file__), 
                         '../../config/db.yml')
    with open(yml_path, 'r') as file:
      config = yaml.load(file, Loader=yaml.FullLoader)
    return psycopg2.connect(dbname=config['database'],
                            user=config['user'],
                            password=config['password'],
                            host=config['host'],
                            port=config['port'])
  
  def __init__(self, schema_name: str):
    self._conn = None
    self._schema = None
    self.open(schema_name)

  def open(self, schema:str=None):
    """Start a new psycopg2 connection if not running"""
    if self._conn is None or self._conn.closed != 0:
      self._conn = self.connect()
      self.set_schema(schema or self._schema)
    else: raise Exception('Connection is already open')

  def set_schema(self, schema:str=None):
    """Set the Postgres `search_path` to a schema"""
    if schema is not None:
      self._schema = schema
    if self._schema is None: return
    with self._conn.cursor() as c:
      c.execute('CREATE SCHEMA IF NOT EXISTS %s;' 
                % self._schema)
      c.execute('SET search_path TO {},public;'
                .format(self._schema))
    self._conn.commit()

  def close(self):
    """Close existing psycopg2 connection"""
    if self._conn.closed == 0:
      self._conn.close()
    else: raise Exception('Connection is already closed')

  def exec_sql_file(self, file: str): 
    """Read a SQL file into the database"""
    # start from root dir, credit swen610_db_utils.py
    abs_path = path.join(path.dirname(__file__), 
                         f'../../{file}') 
    # TODO: should closed connects raise exception
    # or just work automatically?
    if self._conn.closed != 0: self.open()
    with self._conn.cursor() as cursor:
      with open(abs_path, 'r') as file:
        cursor.execute(file.read())
    self._conn.commit()

  def select(self, query:str, args={}, number: int=None):
    """
    Retrieve results of query from database. 
    Does *not* commit.
    """
    result = None
    with self._conn.cursor() as cursor:
      cursor.execute(query, args)
      if number is None:
        result = cursor.fetchall()
      elif number == 1:
        result = cursor.fetchone()
      elif number > 1:
        result = cursor.fetchmany(number)
      else:
        raise ValueError(str(number) 
                          + ' is not a positive integer.')
    self._conn.rollback()
    return result
  
  def exec_commit(self, query: str, args={}):
    """
    Execute a query, commit to the databse 
    and return the result. On exceptions,
    rollback transaction and raise error.
    """
    result = None
    with self._conn.cursor() as c:
      # TODO: what to do when query throws
      # error, raise or continue
      try:
        c.execute(query, args)
        result = c.fetchall()
      except (Exception) as err:
        if err.args [0] != 'no results to fetch':
          self._conn.rollback()
          raise err
    self._conn.commit()
    return (result if result is None or len(result) != 1 
            else result[0])
