import sys
input = sys.stdin.readline

# 1, 2, 3의 합으로 나타내는 방법의 수 구하기
# x: 현재까지 더한 결과
def get_cnt(x):
    global cnt

    # 원하는 수가 만들어진 경우 끝내기
    if x == n:
        cnt += 1
        return

    # 1, 2, 3 더하기
    get_cnt(x + 1)
    if x + 1 < n:
        get_cnt(x + 2)
    if x + 2 < n:
        get_cnt(x + 3)

##################################################

# 테스트 케이스
for _ in range(int(input())):
    # 만들 수
    n = int(input())

    # 1, 2, 3의 합으로 나타내는 방법의 수
    cnt = 0
    get_cnt(0)
    print(cnt)