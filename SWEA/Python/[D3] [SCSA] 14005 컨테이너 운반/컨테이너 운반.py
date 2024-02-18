# 테스트 케이스
for TC in range(1, int(input()) + 1):
    # 컨테이너 수, 트럭 수
    N, M = map(int, input().split())

    # 화물 무게 (내림차순 정렬)
    W = sorted(list(map(int, input().split())), reverse = True)

    # 트럭의 적재용량 (내림차순 정렬)
    T = sorted(list(map(int, input().split())), reverse = True)

    # 이동한 화물의 최대 중량
    res = 0

    # 화물 인덱스
    i = 0

    # 트럭 탐색
    for t in T:
        # 현재 트럭이 담을 수 있는 화물 찾기
        while i < N and W[i] > t:
            i += 1

        # 화물 담기
        if i < N:
            res += W[i]
            i += 1

        # 더 이상 화물이 없는 경우 끝내기
        else:
            break

    print(f'#{TC} {res}')