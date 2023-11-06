from heapq import heappush, heappop
import sys
input = sys.stdin.readline

# 사방 탐색용
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

# 테스트 케이스 번호
T = 1
while T:
    # 동굴의 크기
    N = int(input())

    # 테스트 케이스 끝
    if N == 0:
        break

    # 동굴 정보
    cave = [list(map(int, input().split())) for _ in range(N)]

    # 위치별 최소 잃은 루피
    rupee = [[sys.maxsize] * N for _ in range(N)]
    rupee[0][0] = cave[0][0]

    # 현재까지 잃은 루피, 현재 위치를 담은 최소 힙
    h = []
    heappush(h, (rupee[0][0], 0, 0))

    # 동굴 탐색
    while h:
        # 현재까지 잃은 루피, 현재 위치
        k, r, c = heappop(h)

        # 동굴의 출구에 도착한 경우 끝내기
        if r == N - 1 and c == N - 1:
            print('Problem {}: {}'.format(T, k))
            break

        # 사방 탐색
        for d in range(4):
            # 다음 위치
            nr = r + dr[d]
            nc = c + dc[d]

            # 범위를 벗어난 경우 패스
            if not (0 <= nr < N and 0 <= nc < N):
                continue

            # 더 적은 루피로 다음 위치에 갈 수 있는 경우 힙에 추가
            nk = k + cave[nr][nc]
            if nk < rupee[nr][nc]:
                rupee[nr][nc] = nk
                heappush(h, (nk, nr, nc))

    # 테스트 케이스 번호 갱신
    T += 1
