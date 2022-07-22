from Searching_Candidates.Search import SearchGoogle


def main():
    # Replace with an API for creating the Query
    query = (
        '"Location * Buenos Aires" "Analista" site:linkedin.com/in OR site:linkedin.com/pub -intitle:profiles'
        ' -inurl:"/dir'
    )

    # Initiate Query
    Query = SearchGoogle(query)
    Query.print_query()
    pass


if __name__ == '__main__':
    main()
