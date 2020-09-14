answer = []
maxNum = 30
# don't really understand why, but it seems like it fibonacci
def lineup(num):
    if num == maxNum:
        print(num, answer[-1])
        return answer[-1]

    if num == 1:
        answer.append(2)
    elif num == 2:
        answer.append(3)
    else:
        answer.append(answer[-1] + answer[-2])
    print(num, answer[-1])
    lineup(num+1)

print(lineup(1))
