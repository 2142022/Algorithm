from collections import deque

# 목적지까지 필요한 배터리 교환 최소 횟수 구하기
def bfs():
    # 현재 위치, 배터리 교환 횟수를 담은 큐
    q = deque([(0, 0)])
    while q:
        # 현재 위치, 배터리 교환 횟수
        i, cnt = q.popleft()

        # 갈 수 있는 최대 위치
        for j in range(i + 1, i + M[i] + 1):
            # 목적지인 경우
            if j == N - 1:
                return cnt

            # 다음 위치에서 배터리 교환
            if j < N - 1:
                q.append((j, cnt + 1))

#######################################################33

    # 테스트 케이스 수
T = int(input())
for t in range(1, T + 1):
    # 정류장 수, 정류장 별 배터리 용량
    N, *M = map(int, input().split())

    # 목적지까지 필요한 배터리 교환 최소 횟수
    print(f'#{t} {bfs()}')