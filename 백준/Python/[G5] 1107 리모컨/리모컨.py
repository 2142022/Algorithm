import sys
input = sys.stdin.readline

# 이동하고자 하는 채널
N = int(input())

# 고장난 버튼 개수
M = int(input())

# 고장난 버튼이 없는 경우
if M == 0:
    print(min(abs(N - 100), len(str(N))))
    exit()

# 고장난 버튼
impossible = list(input().split())

# 원하는 채널까지 버튼을 누르는 최소 횟수
min_cnt = abs(N - 100)
i = 0
while i < min_cnt:
    # 원하는 채널에서 i번 +누르기 전 채널
    ch = N - i
    if ch >= 0:
        # 고장난 버튼을 안 눌러도 되는지 체크
        for c in str(ch):
            if c in impossible:
                break
        # 고장난 버튼을 누르지 않아도 되는 경우 최소 횟수 비교
        else:
            cnt = len(str(ch)) + i
            if cnt < min_cnt:
                min_cnt = cnt
                break

    # 원하는 채널에서 i번 -누르기 전 채널
    ch = N + i
    # 고장난 버튼을 안 눌러도 되는지 체크
    for c in str(ch):
        if c in impossible:
            break
    # 고장난 버튼을 누르지 않아도 되는 경우 최소 횟수 비교
    else:
        cnt = len(str(ch)) + i
        if cnt < min_cnt:
            min_cnt = cnt
            break

    i += 1

print(min_cnt)