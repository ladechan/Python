
import unittest 
from mycode import hello_world
class MyFirstTests(unittest.TestCase):
    def test_hello(self):        
        self.assertEqual(hello_world(), 'hello world')

