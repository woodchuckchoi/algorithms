def myDiv(num):
    digits = str(num)
    sumDigit = 0
    for digit in digits:
        sumDigit += int(digit)
    if num % sumDigit == 0:
        return True
    return False

def fib(log):
    log.append(log[-1] + log[-2])

log = [0, 1]
answer = []

cnt = 0
while cnt < 12:
    fib(log)
    if myDiv(log[-1]):
        answer.append(log[-1])
        cnt += 1
print(answer)
