numbers = [1, 14, 14, 4, 11, 7, 6, 9, 8, 10, 10, 5, 13, 2, 3, 15]
sumAll  = sum(numbers)

ary     = [0] * (sumAll+1)
ary[0]  = 1

for num in numbers:
    for i in range(sumAll - num, -1, -1):
        ary[i + num] += ary[i]

print(ary.index(max(ary)))
print(ary)
