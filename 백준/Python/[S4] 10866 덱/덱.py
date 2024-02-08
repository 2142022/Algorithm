from collections import deque
import sys
input = sys.stdin.readline

# 명령의 수
N = int(input())

# 큐
q = deque()

# 명령
for _ in range(N):
    op, *num = input().split()

    if op == 'push_front':
        q.appendleft(num[0])
    elif op == 'push_back':
        q.append(num[0])
    elif op == 'pop_front':
        print(q.popleft() if q else -1)
    elif op == 'pop_back':
        print(q.pop() if q else -1)
    elif op == 'size':
        print(len(q))
    elif op == 'empty':
        print(0 if q else 1)
    elif op == 'front':
        print(q[0] if q else -1)
    else:
        print(q[-1] if q else -1)