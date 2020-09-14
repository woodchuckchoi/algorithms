def binary_search(array, number):
    n = len(array)
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        if number == array[mid]:
            return mid
        elif number > array[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1


d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(d, 36))
print(binary_search(d, 50))