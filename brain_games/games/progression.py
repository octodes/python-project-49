"""Brain progression game logic resource."""


import random


RULES = 'What number is missing in the progression?'


def generate_math_progression():
    """Generate math progression within defined params.

        Returns: list of math progression string elements
    """
    progression_length = random.randint(5, 10)
    element = random.randint(1, 50)
    step = random.randint(2, 6)
    progression = [str(element)]

    for _ in range(1, progression_length):
        element = element + step
        progression.append(str(element))

    return progression


def make_question_and_answer():
    """Generate question and check for right answer.

    Returns:
        question = random math progression with missing element.
        correct_answer = string with missing element.
    """
    progression = generate_math_progression()
    hidden_element_index = random.randint(0, len(progression) - 1)
    correct_answer = progression[hidden_element_index]
    progression[hidden_element_index] = '..'
    question = ' '.join(progression)

    return question, correct_answer
