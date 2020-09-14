n = 16
pos = [0] * (n // 2 + 1)
pos[0] = 1

for i in range(1, n // 2 + 1):
    for j in range(0, i):
        pos[i] += pos[j] * pos[i-j-1]

print(pos[n//2])
