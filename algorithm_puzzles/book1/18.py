from itertools import permutations
from math import sqrt, floor

def checkSquare(num):
    tmp = floor(sqrt(num))
    if tmp * tmp == num:
        return True
    return False

answer = []

def cake(piece, array):
    global answer

    if answer != []:
        return

    if len(array) == piece:
        if checkSquare(array[0] + array[-1]):
	        answer = array
	        return

    for i in range(1, piece + 1):
        if i in array:
            continue
        if checkSquare(array[-1] + i):
            cake(piece, array + [i])
N = 2
while True:
    cake(N, [1])
    if answer != []:
        break
    N += 1
print(answer)
