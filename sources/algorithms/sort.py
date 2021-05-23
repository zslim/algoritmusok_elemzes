def insertion_sort(array):
    result = []
    for element in array:
        if len(result) == 0:
            result.append(element)
        else:
            i = 0
            while i <= len(result) - 1 and element > result[i]:
                i += 1
            result.insert(i, element)
    return result


def bubble_sort(array):
    result = array[:]
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if result[j] > result[j + 1]:
                temp = result[j]
                result[j] = result[j + 1]
                result[j + 1] = temp
    return result
