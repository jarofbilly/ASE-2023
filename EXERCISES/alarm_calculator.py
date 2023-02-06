start = int(input('Time now (hour): '))
duration = int(input('Alarm duration (hours): '))

endTime = start + duration

while endTime > 23:
    endTime -= 24

print(f'Alarm will go off at {endTime} hours')
