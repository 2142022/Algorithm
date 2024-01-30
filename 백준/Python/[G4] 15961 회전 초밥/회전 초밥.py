import sys
input = sys.stdin.readline

# 회전 초밥 벨트에 놓인 접시 수, 초밥의 가짓수, 연속해서 먹는 접시 수, 쿠폰 번호
N, d, k, c = map(int, input().split())

# 초밥 순서
sushi = [int(input()) for _ in range(N)]
sushi += sushi[:k]

# 초밥을 탐색한 마지막 인덱스
idx = [-1] * (d + 1)

# 탐색하는 k개의 초밥의 가짓수 (쿠폰이 있으므로 1로 초기화)
cnt = 1
for i in range(k):
    # 현재 초밥
    s = sushi[i]

    # 아직 먹지 않았다면 추가
    if s != c and idx[s] == -1:
        cnt += 1

    idx[s] = i

# 먹을 수 있는 초밥의 최대 가짓수
max_cnt = cnt

# 1칸씩 옮겨가면서 비교
for i in range(k, N + k):
    # 맨 앞 초밥 빼기
    s = sushi[i - k]
    if s != c and idx[s] == i - k:
        cnt -= 1
        idx[s] = -1

    # 현재 초밥 추가
    s = sushi[i]
    if s != c and idx[s] == -1:
        cnt += 1
    idx[s] = i

    # 가짓수 비교
    max_cnt = max(max_cnt, cnt)

print(max_cnt)
