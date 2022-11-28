import prompt


def greet():
    """Prints welcome message on screen"""
    print('Welcome to the Brain Games!')


def welcome_user():
    """Prompts username and prints welcome message, returns name"""
    name = prompt.string('May I have your name? ')
    name = name.capitalize()
    print(f'Hello, {name}!')
    return name


def main():
    welcome_user()


if __name__ == '__main__':
    main()
