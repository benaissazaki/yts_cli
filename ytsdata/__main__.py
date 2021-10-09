''' The Program's entry point where the CLI will run '''

import yts_api

if __name__ == '__main__':
    query = ''

    while True:
        query = input('\n* Search for a movie: ')
        results = yts_api.list_movies(query_term=query)['movies']
        for r in results:
            print(f"{r['id']}-{r['title']}")