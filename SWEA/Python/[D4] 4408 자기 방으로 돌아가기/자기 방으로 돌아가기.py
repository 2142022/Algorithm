# 테스트케이스 수
T = int(input())
for t in range(1, T + 1):
    # 돌아가야 할 학생들의 수
    N = int(input())

    # 각 열별 학생들이 지나다니는 횟수
    cnt = [0] * 200

    # 한 명씩 탐색
    for _ in range(N):
        # 출발 방, 도착 방
        s, d = map(int, input().split())

        # 각 방의 열 구하기
        s, d = (s - 1) // 2, (d - 1) // 2

        # 작은 방부터 체크
        a, b = min(s, d), max(s, d)
        for i in range(a, b + 1):
            cnt[i] += 1

    print(f'#{t} {max(cnt)}')