import math

num = 1
while True:
    digits = '{:10.10f}'.format(math.sqrt(num))
    if len(set(digits.replace('.', '')[:10])) == 10:
        break
    num += 1
print(num)

num = 1
while True:
    digits = '{:10.10f}'.format(math.sqrt(num))
    if len(set(digits.split('.')[1])) == 10:
        break
    num += 1
print(num)
