import unittest
import requests

base_url = 'http://localhost:4500'

class TestRoot(unittest.TestCase):
  def test_get_returns_hello_world(self):
    """Root endpoint should return string 'Hello world!'"""
    res = requests.get(base_url)
    res_text = res.json() # parse json response
    self.assertEqual(res.status_code, 200, 'Expected status code 200')
    self.assertEqual(res_text, 'Hello world!', 'Expected text response of Hello World')

  def test_post_returns_405_error(self):
    """Post requests are not allowed at root endpoint"""
    res = requests.post(base_url)
    self.assertEqual(res.status_code, 405, 'Expected status code 405')

  def test_put_returns_405_error(self):
    """Put requests are not allowed at root endpoint"""
    res = requests.put(base_url)
    self.assertEqual(res.status_code, 405, 'Expected status code 405')

  def test_delete_returns_405_error(self):
    """Delete requests are not allowed at root endpoint"""
    res = requests.delete(base_url)
    self.assertEqual(res.status_code, 405, 'Expected status code 405')

if __name__ == '__main__':
  unittest.main()