def insertion_sort(array):
    n = len(array)

    if n <= 1: return

    for i in range(n-1):
        for j in range(i+1, n):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

test = [1, 5, 6, 4, 8, 9, 7, 3, 2]
insertion_sort(test)

print(test)

# O(n^2)