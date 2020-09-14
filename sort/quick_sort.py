def quick_sort(array, start, end):
    if end - start <= 0:
        return array

    pivot = array[end]
    i = start

    for j in range(start, end):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[end] = array[end], array[i]

    quick_sort(array, start, i-1)
    quick_sort(array, i+1, end)

test = [1, 5, 6, 4, 8, 9, 7, 3, 2]
quick_sort(test)

print(test)

# O(n logn)