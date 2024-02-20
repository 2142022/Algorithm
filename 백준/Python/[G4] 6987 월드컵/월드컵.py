from itertools import combinations
import sys
input = sys.stdin.readline

# 현재 조별 결과가 가능한 결과인지 확인
def possible():
    # 승, 패의 합
    s = 0

    # 무승부가 있는 나라 수
    cnt = 0
    # 무승부 횟수
    same = 0

    for i in range(0, 18, 3):
        # 승
        s += result[i]

        # 무승부
        if result[i + 1]:
            cnt += 1
            same += result[i + 1]

        # 패
        s -= result[i + 2]

        # 승 + 무승부 + 패가 5가 아닌 경우 불가능
        if sum(result[i:i + 3]) != 5:
            return 0

    # 승, 패의 개수가 다른 경우 불가능
    if s:
        return 0

    # 무승부가 나온 나라가 1개인 경우 불가능
    if cnt == 1:
        return 0

    # 무승부 횟수가 홀수인 경우 불가능
    if same % 2:
        return 0

    return 1

##########################################################

# idx번째 경기 확인
def dfs(idx):
    global flag

    # 이미 가능한 결과로 판단된 경우 끝내기
    if flag:
        return

    # 모든 경기를 다 치룬 경우
    if idx == 15:
        flag = 1
        return

    # 현재 경기 나라
    a, b = play[idx]

    # a: 승, b: 패
    if cnt[a][0] and cnt[b][2]:
        cnt[a][0] -= 1
        cnt[b][2] -= 1
        dfs(idx + 1)
        if flag:
            return
        cnt[a][0] += 1
        cnt[b][2] += 1

    # 무승부
    if cnt[a][1] and cnt[b][1]:
        cnt[a][1] -= 1
        cnt[b][1] -= 1
        dfs(idx + 1)
        if flag:
            return
        cnt[a][1] += 1
        cnt[b][1] += 1

    # a: 패, b: 승
    if cnt[a][2] and cnt[b][0]:
        cnt[a][2] -= 1
        cnt[b][0] -= 1
        dfs(idx + 1)
        if flag:
            return
        cnt[a][2] += 1
        cnt[b][0] += 1

##########################################################

# 각 판이 가능한 결과인지 확인
for _ in range(4):
    # 조별 결과
    result = list(map(int, input().split()))

    # 불가능한 경기인 경우
    if not possible():
        print(0, end = ' ')
        continue

    # 나라별 결과
    cnt = [result[i:i + 3] for i in range(0, 18, 3)]

    # 모든 경기
    play = list(combinations(range(6), 2))

    # 현재 조별 결과가 가능한 결과인지 확인
    flag = 0
    dfs(0)
    print(flag, end = ' ')
