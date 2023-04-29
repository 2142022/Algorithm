import sys
input = sys.stdin.readline

# N번째 피보나치 수를 구할 때 0과 1이 출력되는 횟수 반환
def get_cnt(x):
    # x에 대한 cnt가 있으면 반환
    if x in cnt:
        return cnt[x]

    if x == 0:
        cnt[x] = (1, 0)
        return cnt[x]
    elif x == 1:
        cnt[x] = (0, 1)
        return cnt[x]
    else:
        cnt[x] = (get_cnt(x - 1)[0] + get_cnt(x - 2)[0], get_cnt(x - 1)[1] + get_cnt(x - 2)[1])
        return cnt[x]

#################################################################################################

# 테스트 케이스 개수
T = int(input())

# T개의 테스트 케이스
for _ in range(T):
    # 주어진 수
    N = int(input())

    # cnt[N]: N번째 피보나치 수를 구할 때 출력되는 0과 1의 개수
    cnt = dict()

    # N번째 피보나치 수 구하기
    get_cnt(N)

    print(cnt[N][0], cnt[N][1])