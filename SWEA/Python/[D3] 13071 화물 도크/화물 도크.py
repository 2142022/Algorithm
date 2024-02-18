# 테스트 케이스
for TC in range(1, int(input()) + 1):
    # 신청서 수
    N = int(input())

    # 화물차의 작업 시간 (시작 시간 기준 오름차순 정렬 후, 종료 시간 기준으로 오름차순 정렬)
    A = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[0], x[1]))

    # 마지막 작업의 끝나는 시간
    le = 0

    # 최대 이용한 화물차 수
    cnt = 0

    # 화물차 하나씩 탐색
    for s, e in A:
        # 마지막 작업보다 일찍 끝나는 경우 바꾸기
        if e < le:
            le = e

        # 현재 상태에서 추가할 수 있는 작업인 경우
        elif s >= le:
            le = e
            cnt += 1

    print(f'#{TC} {cnt}')