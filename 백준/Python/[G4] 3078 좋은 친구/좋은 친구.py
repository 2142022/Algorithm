import sys
input = sys.stdin.readline

# 학생 수, 좋은 친구의 최대 등수 차이
N, K = map(int, input().split())

# 좋은 친구의 쌍 수
pair = 0

# 이름의 글자 수별 학생 수
cnt = [0] * 21

# 학생 이름의 글자 수
name = [0] * N

# 한 명씩 탐색
for i in range(N):
    # 좋은 친구의 범위가 아닌 친구 삭제
    if i - K - 1 >= 0:
        cnt[name[i - K - 1]] -= 1

    # 학생 이름의 글자수
    L = len(input().rstrip())
    name[i] = L

    # 좋은 친구 수 갱신
    pair += cnt[L]

    # 이름의 글자 수별 학생 수 갱신
    cnt[L] += 1

print(pair)
