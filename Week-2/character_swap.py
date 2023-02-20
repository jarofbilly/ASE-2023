one = list(input('String one: '))
two = list(input('String two: '))

tempOne = [one[0], one[1]]

one[0], one[1] = two[0], two[1]
two[0], two[1] = tempOne[0], tempOne[1]

print(f'{"".join(one)} {"".join(two)}')
