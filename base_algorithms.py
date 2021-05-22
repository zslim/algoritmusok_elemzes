def intersection(a, b):
    result = []
    n = len(a)
    m = len(b)
    for i in range(n):
        j = 0
        while j < m and a[i] != b[j]:
            j += 1
        if j < m:
            result.append(a[i])
    return result


def union(a: list, b: list):
    result = a
    n = len(a)
    m = len(b)
    for j in range(m):
        i = 0
        while i < n and a[i] != b[j]:
            i += 1
        if i >= n:
            result.append(b[j])
    return result


def merge(a, b):
    result = []
    n = len(a)
    m = len(b)
    i = 0
    j = 0
    while i < n and j < m:
        a_current = a[i]
        b_current = b[j]
        if a_current < b_current:
            result.append(a_current)
            i += 1
        elif a_current == b_current:
            result.append(a_current)
            i += 1
            j += 1
        else:
            result.append(b_current)
            j += 1
    if i >= n:
        result += b[j:]
    else:
        result += a[i:]
    return result


if __name__ == '__main__':
    c = [1, 4, 3, 7, 1]
    d = [0, 1, 6, 9, 3]
    print(intersection(c, d))
    print(intersection([True, True], [False, True]))
    print(union(c, d))

    e = [1, 3, 4, 6, 7]
    f = [2, 4, 6, 8, 10]
    print(merge(e, f))
