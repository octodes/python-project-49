"""Brain progression game logic resource."""


import random


RULES = 'What number is missing in the progression?'


def make_question_and_answer():
    """Generate question and check for right answer.

    Returns:
        question = random math progression with missing element.
        correct_answer = string with missing element.
    """
    progression_length = random.randint(5, 10)
    element = random.randint(1, 50)
    step = random.randint(2, 6)
    progression = [element]

    for _ in range(1, progression_length):

        element = element + step
        progression.append(element)

    hidden_element_position = random.randint(0, progression_length)
    modified_progression = [str(el) for el in progression]
    modified_progression[hidden_element_position] = '..'

    question = ' '.join(modified_progression)
    correct_answer = str(progression[hidden_element_position])

    return question, correct_answer
