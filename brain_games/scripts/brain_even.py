#!/usr/bin/env python3
import random
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


def even_rules_explain():
    """Prints brain-even game rules"""
    print('Answer "yes" if the number is even, otherwise answer "no".')


def even_game(name='Friend'):
    """Asking user is number even and counts to three correct in a row"""
    correct_counter = 0

    while correct_counter < 3:

        question_num = random.randint(1, 1000)
        print(f'Question: {question_num}')
        answer = prompt.string('Your answer: ')

        if question_num % 2 == 0:

            if answer == 'yes':

                print('Correct!')
                correct_counter += 1

            elif answer == 'no':

                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                print(f"Let's try again, {name}!")
                break

            else:

                print("Wrong answer format, please type 'yes' or 'no'.")
                print(f"Let's try again, {name}!")
                break

        elif question_num % 2 != 0:

            if answer == 'no':

                print('Correct!')
                correct_counter += 1

            elif answer == 'yes':

                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                print(f"Let's try again, {name}!")
                break

            else:

                print("Wrong answer format, please type 'yes' or 'no'.")
                print(f"Let's try again, {name}!")
                break

    if correct_counter == 3:
        print(f'Congratulations, {name}')


def main():
    greet()
    name = welcome_user()
    even_rules_explain()
    even_game(name)


if __name__ == '__main__':
    main()
