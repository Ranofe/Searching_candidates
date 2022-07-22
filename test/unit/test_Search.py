import unittest

from Searching_Candidates.Search import SearchGoogle


class TestQuery(unittest.TestCase):
    # test function to test equality of two value
    def test_Query(self):
        query = (
        
            '"Location * Buenos Aires" "Analista" site:linkedin.com/in OR site:linkedin.com/pub -intitle:profiles'
            ' -inurl:"/dir'
        )
        Query = SearchGoogle(query)
        self.assertEqual(query, Query.query, 'Query not equal')
