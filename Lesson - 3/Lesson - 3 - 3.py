import math
random_list: list = [1,23,24,353,4,3,3,53,42,32,25,3]
step_count = int(input())
def shift(always_list: list, count_step : int):
    copy_list_step = []
    count_step %= len(always_list)
    if count_step > 0:
        copy_list_step = always_list[-count_step:]
        always_list = always_list[:-count_step]
        always_list[:0] = copy_list_step
    else:
        copy_list_step = always_list[ 0: -count_step]
        always_list = always_list[-count_step : ]
        always_list.extend(copy_list_step)
    return print(always_list)
shift(random_list, step_count)