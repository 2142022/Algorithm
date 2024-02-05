# M개의 나라의 합이 K인 경우의 수 구하기
# start: 탐색할 수 있는 시작 나라
# select: 현재까지 선택한 나라 수
# sum_k: 현재까지 선택한 나라의 국력의 합
def get_sum(start, select, sum_k):
    global N, M, K, cnt

    # 모든 나라를 선택한 경우 끝내기
    if select == M:
        # 선택한 나라의 국력의 합이 K인 경우, 결과 갱신
        if sum_k == K:
            cnt += 1
        return

    # 나라 선택
    for i in range(start, N - M + select + 1):
        get_sum(i + 1, select + 1, sum_k + A[i])

###########################################################3

# 테스트 케이스 수
T = int(input())
for t in range(1, T + 1):
    # 나라 수, 선택할 나라 수, 찾을 국력의 합
    N, M, K = map(int, input().split())

    # 각 나라의 국력
    A = list(map(int, input().split()))

    # M개의 나라의 국력의 합이 K인 경우의 수
    cnt = 0
    get_sum(0, 0, 0)
    print(f'#{t} {cnt}')