import unittest

from .test_req_utils import test_get, test_post, test_put, test_delete

base_url = 'http://localhost:4500'

class TestRoot(unittest.TestCase):
  def test_get_returns_hello_world(self):
    """Root endpoint should return string 'Hello world!'"""
    content = test_get(self, base_url)
    self.assertEqual(content, 'Hello world!', 'Expected text response of Hello World')

  def test_post_returns_405_error(self):
    """Post requests are not allowed at root endpoint"""
    test_post(self, base_url, expected_status=405)

  def test_put_returns_405_error(self):
    """Put requests are not allowed at root endpoint"""
    test_put(self, base_url, expected_status=405)

  def test_delete_returns_405_error(self):
    """Delete requests are not allowed at root endpoint"""
    test_delete(self, base_url, expected_status=405)

if __name__ == '__main__':
  unittest.main()