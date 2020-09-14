def collatz(num):
    mod = num * 3 + 1
    while not (mod == 1 or mod == num):
        if mod % 2 == 1:
            mod = mod * 3 + 1
        else:
            mod = mod / 2
    if mod == num:
        return 1
    return 0

def main():
    cnt = 0
    for i in range(2, 10001):
        cnt += collatz(i)
    print(cnt)

if __name__ == "__main__":
    main()
