import unittest
from app.models import Sources
Sources=sources.Sources

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Sources class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_sources = Sources(ssssss,'bbbbb','cccccccccc','asdfghjkdfg')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_sources,Sources))


if __name__ == '__main__':
    unittest.main()