import time

def quickSort(arr, l, h):
    if l < h:
        pivot = partition(arr, l, h)
        quickSort(arr, l, pivot-1)
        quickSort(arr, pivot+1, h)

def partition(arr, l, h):
    pivot = arr[h]
    i = j = l
    while j < h:
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1
    arr[i], arr[h] = arr[h], arr[i]
    return i

'''
def quickSort(arr, l, h):
    if l < h:
        pivot = partition(arr, l, h)
        quickSort(arr, l, pivot-1)
        quickSort(arr, pivot+1, h)

def partition(arr, l, h):
    pivot = arr[h]
    i = l
    for j in range(l, h):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[h] = arr[h], arr[i]
    return i
'''
def merge(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left    = arr[:mid]
        right   = arr[mid:]

        merge(left)
        merge(right)

        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def main():
    tmp = [1,6,4,3,4,7,9,45,2,5,7,9,3,1,92,6,9,96,5,3,3, 100]
    tmp2 = tmp.copy()
    tic = time.time()
    quickSort(tmp, 0, len(tmp)-1)
    toc = time.time() - tic
    print(tmp, toc)

    tic = time.time()
    merge(tmp2)
    toc = time.time() - tic
    print(tmp2, toc)

if __name__=='__main__':
    main()