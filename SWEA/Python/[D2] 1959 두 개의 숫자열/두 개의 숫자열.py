# 더 작은 크기의 배열을 한 칸씩 옮겨가며 계산
def sol(a, b, n, m):
    # 서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최대값
    mx = -40000

    # b의 시작 인덱스
    for j in range(m - n + 1):
        # a x b 값
        s = 0
        for i in range(n):
            s += a[i] * b[j + i]

        # 최대값 비교
        mx = max(mx, s)

    return mx

###########################################################

# 테스트 케이스 개수
T = int(input())
for t in range(1, T + 1):
    # A, B의 크기
    N, M = map(int, input().split())

    # A, B
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 더 작은 크기의 배열을 한 칸씩 옮겨가며 계산
    if N <= M:
        mx = sol(A, B, N, M)
    else:
        mx = sol(B, A, M, N)

    print(f'#{t} {mx}')