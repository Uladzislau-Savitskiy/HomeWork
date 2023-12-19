progress = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15 ,16, 17, 18,
            19, 20]
stop = True
min_value = 2520
while stop:
    num = 0
    for i in progress:
      if min_value % i == 0:
        num += 1
        if num == 20:
          stop = False
      else:
        break
    if stop == False:
      break
    min_value += 20
print(min_value)