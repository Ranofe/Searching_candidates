# Create the query for looking for candidates.
import json


class Querier(object):
    """Querier is resposible for creating the google query."""

    def __init__(self, json_file_path):
        self.json_file_path = json_file_path
        self.read_json()
        self.site = 'insite:linkedin.com/in'

    def read_json(self):
        f = open(self.json_file_path, "r")
        self.query_dict = json.load(f)

    def create_query(self):
        site_query = "site:linkedin.com/in"

        title_query = "intitle:"
        title_query += self.sub_query_maker(self.query_dict['Title'])

        query = title_query + " " + site_query
        self.google_query = query
        return query

    def sub_query_maker(self, sub_query_dict):
        subquery = ""
        # Must elements
        if "Must" in sub_query_dict:
            must = sub_query_dict['Must']
            subquery += "("
            for n, element in enumerate(must):
                subquery += element
                if n < (len(must) - 1):
                    subquery += " AND "
            subquery += ")"
        # Options
        if "Optional" in sub_query_dict:
            optional = sub_query_dict['Optional']
            subquery += " AND ("  # Start OR
            for n, element in enumerate(optional):
                subquery += element
                if n < (len(optional) - 1):
                    subquery += " OR "
            subquery += ")"  # End OR
        return subquery
