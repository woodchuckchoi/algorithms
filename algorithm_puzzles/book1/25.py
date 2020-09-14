from itertools import permutations

N = 6

max_cnt = 0
tmp = list(range(1, N))

for l in permutations(tmp, N-1):
    for r in permutations(tmp, N-1):
        path    = []
        left    = 0
        right   = r[0]
        for i in range(0, N-1):
            path.append([left, right])
            left = l[i]
            path.append([left, right])
            if len(r) > i + 1:
                right = r[i + 1]
        path.append([left, 0])
        cnt = 0
        for i in range(0, N * 2 - 1):
            for j in range(i + 1, N * 2 - 1):
                if (path[i][0] - path[j][0]) * (path[i][1] - path[j][1]) < 0:
                    cnt += 1
        max_cnt = max([max_cnt, cnt])

print(max_cnt)
