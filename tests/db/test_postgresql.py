import unittest
from src.db.swen610_db_utils import *

class TestPostgreSQL(unittest.TestCase):

    def test_can_connect(self):
        result = exec_get_one('SELECT VERSION()')
        self.assertTrue(result[0].startswith('PostgreSQL'))

    def test_create_table(self):
        exec_commit("""CREATE TABLE example_table(
        id SERIAL PRIMARY KEY,
        foo TEXT NOT NULL);""")

if __name__ == '__main__':
    unittest.main()