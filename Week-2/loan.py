age = int(input('Age: '))
income = float(input('Annual income: '))
loan = input('Already borrowed? [Y/N] ')
loan = (True if loan.lower() == 'y' else False)

allowed = (age >= 20) & (income >= 21000) & (loan == False)

print(f'The loan can be offered: {allowed}')
