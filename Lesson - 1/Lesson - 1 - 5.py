list_1 = [42, 98, 8, 39, 64, 35, 71, 10, 50, 68, 91,
          38, 69, 14, 88, 98, 89, 79, 44, 37, 2, 64,
          19, 76, 91, 49, 88, 10, 10, 6]
num = int(input())
list_1.append(num)
list_1.sort()
index_num = list_1.index(num)
print(list_1[:index_num])