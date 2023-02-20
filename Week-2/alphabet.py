letter = input('Please enter a letter: ')
classification = 'consonant'

if letter in ['a','e','i','o','u']:
    classification = 'vowel'

print(f"The letter '{letter}' is a {classification}")
