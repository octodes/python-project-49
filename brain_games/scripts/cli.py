import prompt

def welcome_user():
    """Prompts username and prints welcome message"""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name.capitalize()}!')

def main():
    welcome_user()

if __name__ == '__main__':
    main()