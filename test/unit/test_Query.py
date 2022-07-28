import unittest

from Searching_Candidates.Query import Querier


class TestQuery(unittest.TestCase):
    def test_Create_Querier(self):
        file_path = "./test/unit/query_test.json"
        Q = Querier(file_path)
        self.assertEqual(type(Q.query_json_dict) is dict, True, "File not read")

    def test_sub_query_maker(self):
        file_path = "./test/unit/query_test.json"
        q_sub_query = {'Must': ['QA Automation'], 'Optional': ['Ssr', 'Sr']}

        Q = Querier(file_path)
        expected_result = "((QA Automation) AND (Ssr OR Sr))"
        result = Q.sub_query_maker(q_sub_query)
        self.assertEqual(result, expected_result, "Sub query error")

        q_sub_query = {'Must': ['QA Automation']}
        expected_result = "(QA Automation)"
        result = Q.sub_query_maker(q_sub_query)
        self.assertEqual(result, expected_result, "Sub query without options error")

        q_sub_query = {'Must': ['QA Automation'], 'Optional': []}
        expected_result = "(QA Automation)"
        result = Q.sub_query_maker(q_sub_query)
        self.assertEqual(result, expected_result, "Sub query without options error")

        q_sub_query = {'Optional': ['Ssr', 'Sr']}
        expected_result = "(Ssr OR Sr)"
        result = Q.sub_query_maker(q_sub_query)
        self.assertEqual(result, expected_result, "Sub query without must error")

        q_sub_query = {'Must': [], 'Optional': ['Ssr', 'Sr']}
        expected_result = "(Ssr OR Sr)"
        result = Q.sub_query_maker(q_sub_query)
        self.assertEqual(result, expected_result, "Sub query without must error")
