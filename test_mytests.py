import unittest 
from test_mycode import *
class MyFirstTests(unittest.TestCase):
    def test_hello(self):        
        self.assertEqual(hello_world(), 'hello world')
    
    def test_custom_num_list(self):        
        self.assertEqual(len(create_num_list(10)), 10)

    def test_custom_num_list1(self):        
        self.assertEqual(len(create_num_list(11)), 11)

    def test_custom_func_x(self):       
        self.assertEqual(custom_func_x(3,2,3), 54)

    def test_custom_func_x1(self):       
        self.assertEqual(custom_func_x(1,2,5), 55)

