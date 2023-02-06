userMonths = ['January', 'March', 'May','September', 'December']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

while set(userMonths) != set(months):
    print(userMonths)
    newMonth = input('Month: ').capitalize()

    if newMonth in userMonths:
        print('Month already exists')
    elif newMonth in months:
        userMonths.append(newMonth)
    else:
        print('Invalid month')

print('All months have been added!')
print(userMonths)

userMonths.remove('May')
userMonths.remove('September')
userMonths.remove('October')

print(userMonths)
