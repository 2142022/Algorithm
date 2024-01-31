from collections import deque

# 테스트 케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 화덕 크기, 피자 개수
    N, M = map(int, input().split())

    # 피자의 치즈 양
    pizza = deque(map(int, input().split()))

    # 첫 N개의 피자 화덕에 넣기
    remain = deque()
    i = 1
    while i <= N:
        remain.append((i, pizza.popleft()))
        i += 1

    # 피자 하나씩 꺼내보기
    while len(remain) != 1:
        # 현재 피자의 치즈 양 반으로 줄이기
        idx, C = remain.popleft()
        C //= 2

        # 치즈가 모두 녹은 경우 다음 피자 넣기
        if C == 0 and pizza:
            remain.append((i, pizza.popleft()))
            i += 1

        # 치즈가 남은 경우, 다시 큐에 넣기
        elif C:
            remain.append((idx, C))

    print(f'#{t} {remain[0][0]}')
