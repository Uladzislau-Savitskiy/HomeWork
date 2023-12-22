import typing
def fnc_collatca(t: int) -> int:
    set_numbers: set = set()
    max_count: int = 0
    max_number: int = 0

    for i in range(t, 1, -1):
        if i in set_numbers:
            continue
        n: int = i
        count: int = 0
        set_numbers.add(i)
        while i != 1:
            if i % 2 == 0:
                i //= 2
            else:
                i = i * 3 + 1
            if i < t:
                set_numbers.add(i)
            count += 1
        if count > max_count:
            max_count, max_number = count, n
    return max_number

print(fnc_collatca(1000000))
