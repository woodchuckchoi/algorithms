boy     = 20
girl    = 10

arr = []
for g in range(girl + 1):
    arr.append([0] * (boy + 1))
arr[0][0] = 1

for g in range(girl + 1):
    for b in range(boy + 1):
        if g != b and girl - g != boy - b:
            if b > 0:
                arr[g][b] += arr[g][b-1]
            if g > 0:
                arr[g][b] += arr[g-1][b]

print(arr[girl][boy-1] + arr[girl-1][boy])
print(arr)
