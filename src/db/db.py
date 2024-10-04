import psycopg2
import yaml
import os.path as path

class Database():

  @staticmethod
  def connect():
    """Connect to the database with data from ~/config/db.yml"""
    config = {}
    yml_path = path.join(path.dirname(__file__), '../../config/db.yml')
    with open(yml_path, 'r') as file:
      config = yaml.load(file, Loader=yaml.FullLoader)
    return psycopg2.connect(dbname=config['database'],
                            user=config['user'],
                            password=config['password'],
                            host=config['host'],
                            port=config['port'])
  
  def __init__(self):
    self._conn = None
    self.open()

  def open(self):
    """Start a new psycopg2 connection if not running"""
    if self._conn is None or self._conn.closed != 0:
      self._conn = self.connect()
    else: raise Exception('Connection is already open')

  def close(self):
    """Close existing psycopg2 connection"""
    # if self._conn.closed == 0:
    if self._conn is not None:
      self._conn = self._conn.close()
    else: raise Exception('Connection is already closed')

  def exec_sql_file(self, file: str): 
    """Read a SQL file into the database"""
    abs_path = path.join(path.dirname(__file__), f'../../{file}') # start from root dir
    if self._conn.closed != 0: self.open()
    with self._conn.cursor() as cursor:
      with open(abs_path, 'r') as file:
        cursor.execute(file.read())
    self._conn.commit()
