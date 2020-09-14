from itertools import combinations
from math import gcd

maxLen = 500
cnt = 0

for sqr in range(1, maxLen // 4 + 1):
    for a, b in combinations(range(1, sqr), 2):
        if a*a + b*b == sqr*sqr:
	        if gcd(a, b) == 1:
	            cnt += 1

print(cnt)

