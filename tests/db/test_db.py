from src.db.db import Database
import unittest
import psycopg2.extensions as pg_ext

class TestDatabase(unittest.TestCase):
  def setUp(self):
    self.db = Database()

  def tearDown(self):
    if self.db._conn is None or self.db._conn.closed != 0:
      self.db.open()
    with self.db._conn.cursor() as cursor:
      cursor.execute('DROP SCHEMA IF EXISTS test CASCADE;')
    self.db._conn.commit()
    self.db._conn.close()

  def test_init(self):
    self.assertEqual(self.db._conn.status, 
                     pg_ext.STATUS_READY, 
                     'Expected open connection')
  
  def test_open_starts_new_connections_when_closed(self):
    old_connection = self.db._conn
    self.db.close()
    self.assertEqual(self.db._conn, None, 
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
    self.assertEqual(self.db._conn, None,
                     'Connection has closed status')

  def test_exec_sql(self):
    self.db.exec_sql_file('test.sql')
