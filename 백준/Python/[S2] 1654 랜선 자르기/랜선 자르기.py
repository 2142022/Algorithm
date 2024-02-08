import sys
input = sys.stdin.readline

# 만들 수 있는 크기가 L인 랜선의 개수 구하기
def get_cnt(L):
    cnt = 0
    for i in lan:
        cnt += i // L
    return cnt

#########################################################

# 랜선 수, 필요한 랜선 수
K, N = map(int, input().split())

# 모든 랜선의 길이
lan = [int(input()) for _ in range(K)]

# 가능한 랜선의 범위
left, right = 1, max(lan)
while True:
    if left == right:
        print(left)
        break
    elif left + 1 == right:
        if get_cnt(right) == N:
            print(right)
        else:
            print(left)
        break

    # 탐색할 랜선의 길이
    l = (left + right) // 2

    # 현재 길이의 랜선 개수
    cnt = get_cnt(l)

    # 부족하다면 길이를 줄이고, 많다면 길이 늘리기
    if cnt < N:
        right = l
    else:
        left = l
