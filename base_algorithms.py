from timing import timer, TIMES


@timer(TIMES)
def intersection(a_list, b_list):
    result = []
    n = len(a_list)
    m = len(b_list)
    for i in range(n):
        j = 0
        while j < m and a_list[i] != b_list[j]:
            j += 1
        if j < m:
            result.append(a_list[i])
    return result


if __name__ == '__main__':
    a = [1, 4, 3, 7, 1]
    b = [0, 1, 6, 9, 3]
    print(intersection(a, b))
    print(intersection([True, True], [False, True]))
    print(TIMES)
