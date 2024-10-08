import unittest
from src.db.data import *
from src.db.swen610_db_utils import *

class TestData(unittest.TestCase):
  def setUp(self):
    create_test_data()


  def test_data_exists(self):
    """test data exists after being created in setUp"""
    result = does_data_exist('test')
    self.assertTrue(result, 'Expected to find data, but none was found.')
