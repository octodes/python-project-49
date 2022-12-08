"""Brain games engine."""


import prompt


def play(game):
    """Greet user, show rules and run specified brain game.

    Args:
        game: name of current brain game.
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ').capitalize()
    print(f'Hello, {name}!')
    print(game.RULES)

    rounds_count = 3
    current_round = 1

    while current_round <= rounds_count:

        question, correct_answer = game.make_question_and_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:

            print('Correct!')
            current_round += 1

        else:

            print(f"'{answer}' is wrong answer ;(.", end=" ")
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")

            return

    print(f'Congratulations, {name}!')
