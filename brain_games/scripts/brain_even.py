#!/usr/bin/env python3
from brain_games.scripts.brain_games import greet
from brain_games.cli import welcome_user


def rules_explain():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def main():
    greet()
    welcome_user()
    rules_explain()


if __name__ == '__main__':
    main()