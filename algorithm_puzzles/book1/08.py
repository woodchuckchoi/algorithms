possible=((0, 1), (0, -1), (1, 0), (-1, 0))
step=12

def move(log):
    global possible

    if len(log) == step + 1:
        return 1

    cnt = 0

    for p in possible:
        nextP = [log[-1][0]+p[0], log[-1][1]+p[1]]
        if nextP in log:
            continue
        cnt += move(log+[nextP])

    return cnt

print(move([[0,0]]))

