"""Brain gcd game logic resource."""


import random
import math


RULES = 'Find the greatest common divisor of given numbers.'


def make_question_and_answer():
    """Generate question and check for right answer.

    Returns:
        question = two random generated numbers in range [1..50].
        correct_answer = string with answer to expression.
    """

    num_1 = random.randint(1, 50)
    num_2 = random.randint(1, 50)
    question = f'{num_1} {num_2}'
    correct_answer = str(math.gcd(num_1, num_2))

    return question, correct_answer
