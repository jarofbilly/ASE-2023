import random

words = ['experienced', 'requirement', 'performance', 'organisation', 'preparation', 'consolidate', 'conservative', 'legislature', 'preoccupation', 'rehabilitation']

wrong = 0
word = list(random.choice(words))

while wrong < 9:
    guess = input('Guess a letter').lower()
    if guess in word:
        print(f"The letter '{guess} is in the word'")
    else:
        wrong += 1
        print(f'That is an incorrect guess.\nYou have {9-wrong} guesses remaining.')
