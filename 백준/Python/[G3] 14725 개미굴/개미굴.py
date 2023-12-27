import sys
input = sys.stdin.readline

# 정보 개수
N = int(input())

# 먹이 정보 (사전순으로 정렬)
food = []
for _ in range(N):
    info = input().rstrip()
    idx = info.index(' ')
    food.append(info[idx + 1:])
food.sort()

# 이미 출력한 먹이 정보
already = set()

# 정보 하나씩 탐색
for info in food:
    # 정보 길이
    M = len(info)

    # 공백 개수
    cnt = 0

    # 먹이 탐색
    i = 0
    while i < M:
        # 먹이 이름
        name = ''
        while i < len(info) and info[i] != ' ':
            name += info[i]
            i += 1

        # 아직 출력하지 않은 경우 출력
        if i == M:
            check = info
        else:
            check = info[:i]
        if check not in already:
            # 공백 + 먹이 이름 출력
            print('--' * cnt + name)
            already.add(check)

        cnt += 1
        i += 1
