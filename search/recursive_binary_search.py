def binary_search(array, number, idx):
    n = len(array)
    
    if n <= 0: return -1

    start = 0
    end = n - 1

    mid = (end + start) // 2

    print(f'mid is {array[mid]}')

    if array[mid] == number:
        return mid + idx
    elif array[mid] > number:
        return binary_search(array[:mid], number, idx)
    else:
        return binary_search(array[mid+1:], number, mid + 1)

d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(d, 36, 0))
print(binary_search(d, 50, 0))