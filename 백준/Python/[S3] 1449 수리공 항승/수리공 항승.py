from collections import deque
import sys
input = sys.stdin.readline

# N: 물이 새는 곳의 개수, L: 테이프의 길이
N, L = map(int, input().split())

# 물이 새는 곳의 위치
tmp = list(map(int, input().split()))

# 오름차순 정렬
tmp.sort()

# list를 deque로 만들기
leak = deque(tmp)

# 테이프의 개수
cnt = 0

# 한 곳씩 확인
while leak:
    # 현재 위치
    now = leak.popleft()

    # 개수 증가
    cnt += 1

    # L - 1의 길이만큼 새는 곳 막기
    while leak:
        if leak[0] <= now + L - 1:
            leak.popleft()
        else:
            break

print(cnt)