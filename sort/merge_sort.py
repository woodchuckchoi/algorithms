def merge_sort(array):
    n = len(array)
    if n <= 1: return

    mid = n // 2

    a1 = array[:mid]
    a2 = array[mid:]

    merge_sort(a1)
    merge_sort(a2)

    i1, i2, ia = 0, 0, 0

    while i1 < len(a1) and i2 < len(a2):
        if a1[i1] < a2[i2]:
            array[ia] = a1[i1]
            ia += 1
            i1 += 1
        else:
            array[ia] = a2[i2]
            ia += 1
            i2 += 1
    
    while i1 < len(a1):
        array[ia] = a1[i1]
        ia += 1
        i1 += 1
    
    while i2 < len(a2):
        array[ia] = a2[i2]
        ia += 1
        i2 += 1

test = [1, 5, 6, 4, 8, 9, 7, 3, 2]
merge_sort(test)

print(test)

# O(n logn)