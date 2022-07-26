from random import randint

DESCRIPTION = 'Answer "yes" if number is even otherwise answer "no".'
START_NUMBER = 1
END_NUMBER = 101


def get_round():
    number = randint(START_NUMBER, END_NUMBER)
    question = f'{number}'
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
