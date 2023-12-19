string = input()
evan = 0
odd = 0
index = 0
for i in string:
  num = int(string[index])
  if num % 2:
    evan += 1
    index += 1
  else:
    odd += 1
    index += 1
print('Количество четных числен равно =', evan)
print('Количество нечетных числен равно =', odd)