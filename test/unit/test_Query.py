import unittest

from Searching_Candidates.Query import Querier


class TestQuery(unittest.TestCase):
    def test_Create_Querier(self):
        file_path = "./example/query_example.json"
        Q = Querier(file_path)
        self.assertEqual(type(Q.query_dict) is dict, True, "File not read")

    def test_sub_query_maker(self):
        file_path = "./example/query_example.json"
        q_sub_query = {'Must': ['QA Automation'], 'Optional': ['Ssr', 'Sr']}

        Q = Querier(file_path)
        expected_result = "(QA Automation) AND (Ssr OR Sr)"
        result = Q.sub_query_maker(q_sub_query)
        self.assertEqual(result, expected_result, "Sub query error")

        q_sub_query = {'Must': ['QA Automation']}
        expected_result = "(QA Automation)"
        result = Q.sub_query_maker(q_sub_query)
        self.assertEqual(result, expected_result, "Sub query without options error")

        # TODO: Tests without must and optinoal
        # q_sub_query = {'Must': ['QA Automation'], 'Optional':[]}
        # expected_result = "(QA Automation)"
        # result = Q.sub_query_maker(q_sub_query)
        # self.assertEqual(result, expected_result, "Sub query without options error")
