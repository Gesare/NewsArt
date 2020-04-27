import unittest
from app.models import Source,News_Article  
import datetime

class Source_Test(unittest.TestCase):
    '''
    Source test class to test the behavior of Source class.
    '''
    def setUp(self):
        '''
        Set up method to create an instance of a source before any test.
        '''
        self.new_source = Source("abc-news","ABC NEWS","Your trusted source for breaking news and analysis.")
    
    def test_instance(self):
        '''
        Test instance method to test if objects are iniatialized properly.
        '''
        self.assertTrue(isinstance(self.new_source, Source))

class News_Article_Test(unittest.TestCase):
    '''
    News article test class to test the behavior of News Article class.
    '''
    def setUp(self):
        '''
        '''
        self.new_article = News_Article("1","Ray","Superman's Metropolis", "efef efefe fefe fefe", datetime.date.today(),"","","")
    
    def test_instance(self):
        '''
        '''
        self.assertTrue(isinstance(self.new_article,News_Article))

