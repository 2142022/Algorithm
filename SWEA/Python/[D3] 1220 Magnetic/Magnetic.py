# 테스트케이스
for t in range(1, 11):
    # 테이블 한 변의 길이
    N = int(input())

    # 테이블
    table = [list(map(int, input().split())) for _ in range(N)]

    # 교착 상태 개수
    cnt = 0

    # 한 열씩 탐색
    for j in range(N):
        # 마지막으로 탐색한 자성체 정보
        last = -1
        for i in range(N):
            # 첫 N극이 나온 경우
            if last == -1:
                if table[i][j] == 1:
                    last = 1

            # 마지막으로 탐색한 자성체가 N극이면서 현재 자성체가 S극인 경우, 교착 상태
            elif last == 1 and table[i][j] == 2:
                last = 2
                cnt += 1

            # 마지막으로 탐색한 자성체가 S극이면서 현재 자성체가 N극인 경우, 교착 상태의 시작점
            elif last == 2 and table[i][j] == 1:
                last = 1

    print(f'#{t} {cnt}')