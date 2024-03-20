from itertools import combinations
from collections import defaultdict
import sys
input = sys.stdin.readline

# 읽을 수 있는 단어 최대 개수 구하기
def find_cnt():
    # 필요한 단어 개수보다 고를 수 있는 글자 수가 큰 경우 모든 단어 읽을 수 있음
    if len(alpha.keys()) <= K - 5:
        return N

    # 읽을 수 있는 단어 최대 개수 (처음부터 읽을 수 있는 단어 개수로 초기화)
    already = complete.count(0)
    max_cnt = already

    # K - 5개 고르기 (-5: antic)
    for combs in combinations(alpha.keys(), K - 5):
        # 읽을 수 있는 단어 개수
        cnt = already

        # 각 단어에서 읽을 수 있는 글자 체크
        words = [0] * N

        # 읽을 수 있는 글자
        for c in combs:
            # 현재 글자가 포함된 단어
            for i in alpha[c]:
                words[i] |= 1 << c

                # 현재 단어를 읽을 수 있는 경우
                if words[i] == complete[i]:
                    cnt += 1

        max_cnt = max(max_cnt, cnt)
        if max_cnt == N:
            return N

    return max_cnt

##############################################################################

# 단어 개수, 가르칠 수 있는 글자 개수
N, K = map(int, input().split())

# 'antic'을 제외한 알파벳이 영향을 주는 단어 번호
alpha = defaultdict(list)

# 각 단어에 필요한 알파벳 (비트마스킹) ('antic'을 제외)
complete = [0] * N
for i in range(N):
    word = set(map(lambda x: ord(x) - ord('a'), input().rstrip()))
    for c in word:
        # 'antic' 제외
        if c not in (0, 2, 8, 13, 19):
            alpha[c].append(i)
            complete[i] |= 1 << c

# K가 5개 미만인 경우 모든 단어를 읽을 수 없음
if K < 5:
    print(0)

else:
    # 읽을 수 있는 단어 최대 개수
    print(find_cnt())

