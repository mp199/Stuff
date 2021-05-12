for x in range(1, 6):
    for y in range(1, 6):
        print('x', end='')
    print()

numbers = [2, 4, 1, 6, 8, 2, 1, 4, 9, 3, 5, 6, 2]
frequency = {}
ordered_frequency = []
for n in numbers:
    if n not in frequency:
        frequency[n] = 1
    else:
        frequency[n] += 1
for k, v in frequency.items():
    ordered_frequency.append((v, k))
ordered_frequency.sort(reverse=True)
print(f'The most common number to appear in this list is number {ordered_frequency[0][1]} which appears '
      f'{ordered_frequency[0][0]} times')
