"""Brain calc game logic resource."""


import random
import operator


RULES = 'What is the result of the expression?'
OPERATORS_LIST = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}


def make_question_and_answer():
    """Generate question and check for right answer.

    Returns:
        question = random generated expression with numbers in range [1..10].
        correct_answer = string with answer to expression.
    """

    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    operation = random.choice(list(OPERATORS_LIST.keys()))
    question = f'{num_1} {operation} {num_2}'
    correct_answer = str(OPERATORS_LIST[operation](num_1, num_2))

    return question, correct_answer
