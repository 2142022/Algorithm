from collections import Counter
import sys
input = sys.stdin.readline

# 행별로 정렬하기
def sorting():
    # 가장 큰 가로 길이
    L = 0

    # 행
    for i, a in enumerate(A):
        # 현재 행에 있는 숫자와 개수 (개수, 숫자 순으로 오름차순 정렬)
        cnt = sorted([(k, v) for k, v in dict(Counter(a)).items() if k != 0], key = lambda x: (x[1], x[0]))

        # 새로운 행의 원소 개수
        l = 0

        # 새로운 행
        A[i] = []
        for k, v in cnt:
            A[i].append(k)
            A[i].append(v)
            l += 2

            # 100개까지만 저장
            if l == 100:
                break

        # 열 개수 비교
        L = max(L, l)

    # 빈 칸은 0으로 채우기
    for a in A:
        a += [0] * (L - len(a))

#####################################################################################################################

# A[R][C]에 들어있는 값이 K가 되기 위한 연산의 최소 시간 구하기
def get_time():
    global A

    # 최대 100번 반복
    for time in range(101):
        # 행, 열 크기 비교 -> R 연산 / C 연산 선택
        N, M = len(A), len(A[0])

        # A[R][C] = K가 되면 끝내기
        if R < N and C < M and A[R][C] == K:
            return time

        # R 연산
        if N >= M:
            # 정렬하기
            sorting()

        # C 연산
        else:
            # 시계방향 90도 회전
            A = list(map(list, zip(*A[::-1])))

            # 정렬하기
            sorting()

            # 뒤집기
            A = list(map(list, zip(*A)))

    # 100초가 지나도 A[R][C] = K가 되지 않는 경우
    else:
        return -1

########################################################################

# 찾아야하는 곳의 위치와 숫자
R, C, K = map(int, input().split())
R -= 1
C -= 1

# 배열
A = [list(map(int, input().split())) for _ in range(3)]

# A[R][C]에 들어있는 값이 K가 되기 위한 연산의 최소 시간
print(get_time())