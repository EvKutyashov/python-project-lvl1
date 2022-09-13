from random import randint

DESCRIPTION = 'Answer "yes" if number is even otherwise answer "no".'


def get_round():
    number = randint(1, 101)
    question = f'Question: {number}'
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer