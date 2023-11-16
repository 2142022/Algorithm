from collections import defaultdict
import sys
input = sys.stdin.readline

# 게임 수
T = int(input())
for _ in range(T):
    # 문자열
    W = input().rstrip()
    # 특정 문자의 개수
    K = int(input())

    # 특정 문자를 K개 포함하는 최소 문자열의 길이, 최대 문자열의 길이
    minL, maxL = sys.maxsize, 0

    # 각 알파벳의 위치
    idx = defaultdict(list)
    for i in range(len(W)):
        # 현재 문자
        c = W[i]
        idx[c].append(i)

        # 현재 문자가 K개 이상인 경우, 최소 문자열의 길이와 최대 문자열의 길이 갱신
        if len(idx[c]) >= K:
            # 현재 위치의 문자를 포함했을 때의 문자열의 길이
            L = idx[c][-1] - idx[c][-K] + 1
            minL = min(minL, L)
            maxL = max(maxL, L)

    # 만족하는 문자열이 없는 경우
    if minL == sys.maxsize or maxL == 0:
        print(-1)
    else:
        print(minL, maxL)