pos = [[1, 2], [2, 3], [3, 6], [6, 9], [8, 9], [8, 7], [7, 4], [4, 1]]
for i in range(1, 10):
    pos.append([i])

memo = {"[]": 1}
def strike(board):
    key = str(board)
    if key in memo:
        return memo[key]
    cnt = 0
    for b in board:
        next_board = filter(lambda i: len(set(b).intersection(set(i))) == 0, board)
        next_board = list(next_board)
        cnt += strike(next_board)
    memo[key] = cnt
    return cnt

print(strike(pos))
