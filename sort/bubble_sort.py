def bubble_sort(array):
    n = len(array)

    if n <= 1: return

    for i in range(n):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

test = [1, 5, 6, 4, 8, 9, 7, 3, 2]
bubble_sort(test)

print(test)

# O(n^2)