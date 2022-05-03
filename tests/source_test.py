import unittest

class Sources:
    '''
    News Sources class to define news source objects
    '''

    def __init__(self,id,name,category,description):
        self.id = id
        self.name = name
        self.category = category
        self.description = description
        
class TestSources(unittest.TestCase):
    '''
    Test class that defines test cases for the Sources class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_source = Sources("abc-news","ABC-NEWS","sports","") # create a source object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_source.id,"abc-news")
        self.assertEqual(self.new_source.name,"ABC-NEWS")
        self.assertEqual(self.new_source.category,"sports")
        self.assertEqual(self.new_source.description,"")


if __name__ == '__main__':
    unittest.main()