score = int(input('Score (0-100): '))

if not (0 <= score <= 100):
    print('Invalid')
elif (0 <= score < 30):
    print('D')
elif (30 <= score < 50):
    print('C')
elif (50 <= score < 70):
    print('B')
elif (70 <= score <= 100):
    print('A')
