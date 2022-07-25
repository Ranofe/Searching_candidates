import unittest

from Searching_Candidates.Search import SearchGoogle


class TestQuery(unittest.TestCase):
    def test_Query(self):
        query = (
            '"Location * Buenos Aires" "Analista" site:linkedin.com/in OR site:linkedin.com/pub -intitle:profiles'
            ' -inurl:"/dir'
        )
        Query = SearchGoogle(query)
        self.assertEqual(query, Query.query, 'Query not equal')

    def test_google_search(self):
        query = "Racing Club Avellaneda"
        Search = SearchGoogle(query)
        output = Search.google_search()
        # self.assertGreater(len(output), 0, "Searching not working")
        # result = output[0]['text'].find(query.split()[0])
        # self.assertGreaterEqual(result, 0, "Search didn't work")
