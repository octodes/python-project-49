#!/usr/bin/env python3
import cli

def greet():
    """Prints welcome message on screen"""
    print('Welcome to the Brain Games!')

def main():
    greet()
    cli.welcome_user()

if __name__ == '__main__':
    main()
