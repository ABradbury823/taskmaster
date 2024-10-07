import unittest
from src.db.swen610_db_utils import *

class TestPostgreSQL(unittest.TestCase):

    def test_can_connect(self):
        result = exec_get_one('SELECT VERSION()')
        self.assertTrue(result[0].startswith('PostgreSQL'))

if __name__ == '__main__':
    unittest.main()