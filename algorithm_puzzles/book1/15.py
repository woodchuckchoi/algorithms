steps=10
maxStep=4
memo = {}

def step(a, b):
    if a > b:
        return 0

    if a == b:
        return 1

    key = (a, b)
    if key in memo:
        return memo[key]

    cnt = 0
    
    for aStep in range(1, maxStep+1):
        for bStep in range(1, maxStep+1):
            cnt += step(a + aStep, b - bStep)

    memo[key] = cnt
    return cnt

print(step(0, steps))
