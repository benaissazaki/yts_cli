from PyInquirer import prompt

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
    pass

