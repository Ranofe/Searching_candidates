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
        self.query_json_dict = json.load(f)

    def create_query(self):
        self.query = self.site + " "
        self.query_dict = {}

        for key in self.query_json_dict:
            query_aux = ""
            if key == 'Title':
                query_aux = "intitle:"
            query_aux += self.sub_query_maker(self.query_json_dict[key])
            self.query_dict[key] = query_aux
            self.query += query_aux + " "
        self.google_query = self.query
        return self.query

    def sub_query_maker(self, sub_query_dict):
        subquery = ""
        must = 0  # indicates there is a must term
        optional = 0  # indicates there is an optional term
        # Must elements
        if "Must" in sub_query_dict:
            if len(sub_query_dict['Must']) > 0:
                must = sub_query_dict['Must']
                subquery += "("
                for n, element in enumerate(must):
                    subquery += element
                    if n < (len(must) - 1):
                        subquery += " AND "
                subquery += ")"
                must = 1
        # Options
        if "Optional" in sub_query_dict:
            if len(sub_query_dict['Optional']) > 0:
                optional = sub_query_dict['Optional']
                if must != 0:
                    subquery += " AND ("  # Start OR
                else:
                    subquery += "("
                for n, element in enumerate(optional):
                    subquery += element
                    if n < (len(optional) - 1):
                        subquery += " OR "
                subquery += ")"  # End OR
                optional = 1
        if must and optional:
            subquery = "(" + subquery + ")"
        return subquery
