from itertools import permutations

def prime(num):
    if num <= 1:
        return False
    elif 1 < num <= 2:
        return True

    divider = 2
    end     = (num // divider) + 1
    while end > divider:
        if num % divider == 0:
            return False
        divider += 1
        end = (num // divider) + 1
    return True

primes = []

start = 2
while len(primes) != 6:
    if prime(start):
        primes.append(start)
    start += 1
        

print(primes)
min_val = primes[-1] * primes[-1]
min_friend = []
for prime in permutations(primes):
    friends = [prime[i] * prime[i+1] for i in range(len(prime) - 1)]
    friends += [prime[0] ** 2, prime[-1] ** 2]
    if min_val > max(friends):
        min_val = max(friends)
        min_friend = friends
print(min_val)
min_friend.sort()
print(min_friend)

