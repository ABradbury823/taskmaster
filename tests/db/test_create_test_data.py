import unittest
from src.db.data import *
from src.db.swen610_db_utils import *

class TestCreateTestData(unittest.TestCase):
  def setUp(self):
    exec_sql_file('src/db/create_test_data.sql')


  def test_data_exists(self):
    """test data exists after being created in setUp"""
    result = does_data_exist('test')
    self.assertTrue(result, 'Expected to find data, but none was found.')
