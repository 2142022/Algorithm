# 테스트 케이스 수
T = int(input())
for t in range(1, T + 1):
    # 구역 크기
    N = int(input())

    # 활화산 정보
    info = [list(map(int, input().split())) for _ in range(N)]

    # 활화산 개수, 활화산 최대 위험도, 활화산 최소 위험도
    cnt, mx, mn = 0, 0, 10

    # 사방 탐색용
    dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

    # 탐색 위치
    for r in range(1, N - 1):
        for c in range(1, N - 1):
            # 현재 위치의 위험도
            risk = info[r][c]

            # 사방 탐색
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]

                # 현재 위험도보다 큰 경우 끝내기
                if info[nr][nc] >= risk:
                    break

            # 현재 위치를 활화산으로 지정
            else:
                cnt += 1
                mx = max(mx, risk)
                mn = min(mn, risk)

    # 활화산이 1개 이하인 경우 -1 출력
    if cnt <= 1:
        print(f'#{t} -1')
    else:
        print(f'#{t} {mx - mn}')
