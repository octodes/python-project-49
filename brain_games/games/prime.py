"""Brain prime game logic resource."""

import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """Check if argument is prime number.

        Returns:
            Bool. True if number is prime.
    """
    if number < 2:

        return False

    for i in range(3, int(number / 2) + 1):

        if number % i == 0:

            return False

    return True


def make_question_and_answer():
    """Generate question and check for right answer.

    Returns:
        question = random generated integer number in range [1..100].
        correct_answer = 'yes' || 'no' string.
    """
    question = random.randint(1, 100)

    correct_answer = 'yes' if is_prime(question) else 'no'

    return question, correct_answer
