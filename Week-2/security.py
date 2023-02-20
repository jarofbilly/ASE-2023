password = input('Enter a password: ')
retry = input('Re-enter password: ')

if password == retry:
    print('Passwords match!')
else:
    print('Passwords do not match!')
