import unittest
from seed import connect_db, create_database, connect_to_prodev, create_table

class TestDBSetup(unittest.TestCase):
    def test_connection(self):
        conn = connect_db()
        self.assertIsNotNone(conn)
        conn.close()

    def test_prodev_connection(self):
        conn = connect_to_prodev()
        self.assertIsNotNone(conn)
        conn.close()

if __name__ == '__main__':
    unittest.main()
