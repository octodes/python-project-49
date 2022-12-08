"""Brain even game logic resource."""


import random


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_question_and_answer():
    """Generate question and check for right answer.

    Returns:
        question = random generated integer number in range [1..100].
        correct_answer = 'yes' || 'no' string.
    """
    question = random.randint(1, 100)

    correct_answer = 'yes' if question % 2 == 0 else 'no'

    return question, correct_answer
