start = int(input('Starting day: '))
duration = int(input('Duration: '))

endDay = start + duration

while endDay > 6:
    endDay -= 7

print(f'You will return on weekday {endDay}')
