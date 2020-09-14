# sliding window solution
# such a shame that i did not know about dequeue

from collections import deque

def solution(arr, window):
    q = deque()
    globalMax = 0

    for i in range(window):
        while q and arr[i] < arr[q[-1]]:
            q.pop()

        q.append(i)

    for i in range(window, len(arr)):
        globalMax = max(globalMax, arr[q[0]])

        while q and q[0] <= i - window:
            q.popleft()

        while q and arr[i] < arr[q[-1]]:
            q.pop()

        q.append(i)

    print(globalMax)

if __name__ == '__main__':
    arr = [12, 1, 78, 90, 57, 89, 56, 32, 53, 12, 66, 22, 53, 14, 0, 72, 53]
    window = 3
    solution(arr, window)