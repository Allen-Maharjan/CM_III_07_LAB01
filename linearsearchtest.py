#using linear search

import unittest

def linear_search(data , a):
    for i in range (0,len(data)):
        if(data[i] == a):
            return i
            break
    return False
        
class TestSearch(unittest.TestCase):
    
    def test_search(self):
        data = [0,1,2,3,4,5,6,7,8,9]
        self.assertEqual(linear_search(data,6),6)
        self.assertEqual(linear_search(data,11),False)
        
    def test_searchchar(self):
        data = ['a','b','c','d']
        self.assertEqual(linear_search(data,'a'),0)
        self.assertEqual(linear_search(data,'e'),False)
    
if __name__ == '__main__':
    unittest.main()
