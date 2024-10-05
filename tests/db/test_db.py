from src.db.db import Database
import unittest
import psycopg2.extensions as pg_ext
from psycopg2.errors import InFailedSqlTransaction

test_schema = 'test'
class TestDatabase(unittest.TestCase):
  def setUp(self):
    self.db = Database(test_schema)

  def tearDown(self):
    if self.db._conn is None or self.db._conn.closed != 0:
      self.db.open()
    with self.db._conn.cursor() as cursor:
      cursor.execute('DROP SCHEMA IF EXISTS {} CASCADE;'
                      .format(test_schema))
    self.db._conn.commit()
    self.db._conn.close()

  def test_init(self):
    """Initializing db opens connection"""
    self.assertEqual(self.db._conn.status, 
                     pg_ext.STATUS_READY, 
                     'Expected open connection')
  
  def test_open_starts_new_connection_when_closed(self):
    """Initializing db opens connection"""
    old_connection = self.db._conn
    self.db._conn.close()
    self.assertEqual(self.db._conn.closed, 1, 
                     'Expected connection to be closed')
    self.db.open()
    self.assertEqual(self.db._conn.status, 
                     pg_ext.STATUS_READY, 
                     'Expected open connection')
    self.assertNotEqual(self.db._conn, 
                        old_connection, 
                        'Expected new connection object')

  def test_open_does_not_restart_connection(self):
    with self.assertRaises(Exception) as open_conn:
      self.db.open()
    self.assertEqual(open_conn.exception.args[0], 
                     'Connection is already open', 
                     'Expected open connection to throw error')
    
  def test_close(self):
    self.db.close()
    self.assertEqual(self.db._conn.closed, 1,
                     'Connection has closed status')

  def test_exec_sql(self):
    self.db.exec_sql_file('test.sql')
    result = None
    with self.db._conn.cursor() as c:
      c.execute('SELECT * FROM {}.example;'.format(test_schema))
      result = c.fetchall()
      self.assertRaisesRegex(Exception, 'does not exist', c.execute, 
                             'SELECT * FROM public.example;')
    # need to commit, rollback or close connection after any cursor 
    # activity or will have hanging transaction
    # TODO: research autocommit or autorollback
    self.db._conn.rollback() 
    self.assertEqual(result, [('sample', 1)], 
                     'Expected table entity to be returned')
