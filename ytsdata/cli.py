from PyInquirer import prompt
from yts_api import list_movies

def run():
    main_prompt = {
        'type': 'list',
        'name': 'action',
        'message': 'What do you want to do?',
        'choices': [
            'Search a movie',
            'Get a movie\'s details',
            'Get suggestions',
            'Get reviews',
            'Exit'
        ]
    }
    action = ''
    while True:
        action = prompt(main_prompt)['action']
        if action == 'Exit':
            return 0
        treat_action(action)
        

def treat_action(action):
    switch = {
        'Search a movie': search
    }

    instruction = switch.get(action)
    instruction()


def search():
    search_prompt = {
        'type': 'input',
        'name': 'query',
        'message': 'Which movie are you looking for?'
    }
    
    query = prompt(search_prompt)['query']
    results = list_movies(query_term=query)
    if results['movie_count'] == 0:
        print('\nNo movie found.\n')
        return
    print()
    for movie in results['movies']:
        print(f"#{movie['id']}-{movie['title']}")
    print()