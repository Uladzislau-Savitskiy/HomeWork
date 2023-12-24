first, last = 1, 0
while True:
    sum = first
    if sum >= 1_000_000:
        break
    first = sum + last
    last = sum
    print(sum, end=' ')
print(f'\n{last}')
