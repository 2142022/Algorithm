from collections import defaultdict
import sys
input = sys.stdin.readline

# 접시 수, 초밥 가짓수, 연속해서 먹는 접시 수, 쿠폰 번호
N, d, k, c = map(int, input().split())

# 초밥 순서
sushi = [int(input()) for _ in range(N)]
# 두 배로 늘리기
sushi += sushi

# 초밥을 최신에 골랐을 때의 위치
select = defaultdict(int)

# 먹을 수 있는 초밥의 가짓수 (c는 무조건 먹을 수 있으므로 1로 초기화)
cnt = 1

# 첫 k개의 초밥 탐색
for i in range(k):
    # 현재 초밥
    num = sushi[i]

    # 아직 고르지 않은 초밥이며 c가 아닌 경우, 가짓수 증가
    if num != c and num not in select:
        cnt += 1

    # 초밥의 최신 위치 갱신
    select[num] = i

# 먹을 수 있는 초밥의 최대 가짓수
max_cnt = cnt

# 시작 초밥
for i in range(1, N):
    # 맨 앞의 초밥(sushi[i-1]) 삭제
    # 이후에 똑같은 초밥을 고르지 않았다면 cnt 감소
    # 단, c가 아닌 경우에만 감소
    num = sushi[i - 1]
    if num != c and select[num] == i - 1:
        cnt -= 1

    # 초밥 1개(sushi[i+k-1]) 추가
    # 고르지 않은 초밥이며 c가 아닌 경우, 가짓수 증가
    num = sushi[i + k - 1]
    if num != c and (num not in select or select[num] < i):
        cnt += 1

    # 마지막 초밥의 위치 갱신
    select[num] = i + k - 1

    # 초밥의 최대 가짓수 갱신
    max_cnt = max(max_cnt, cnt)

print(max_cnt)
