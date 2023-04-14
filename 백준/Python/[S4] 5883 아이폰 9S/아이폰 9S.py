import sys
input = sys.stdin.readline

# 사람 수
N = int(input())

# N명의 사람이 원하는 용량
B = []
for _ in range(N):
    B.append(int(input()))

# 모든 용량
all = set(B)

# 가장 긴 연속 구간의 길이
result = 1

# 줄에서 뺄 용량 선택해서 반복
for i in all:
    # 현재까지 연속된 연속 구간의 길이
    cnt = 1

    # 이전까지 연속된 용량
    volume = -1

    # N명의 사람 탐색
    for j in range(N):
        # 제외한 사람은 넘어가기
        if B[j] == i:
            continue

        # 용량이 연속된 경우
        if B[j] == volume:
            cnt += 1
        # 용량이 연속되지 않은 경우
        else:
            result = max(result, cnt)
            cnt = 1
            volume = B[j]

    # 끝까지 연속하는 경우를 위해 한 번 더 비교
    result = max(result, cnt)

print(result)