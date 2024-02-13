from collections import defaultdict
import sys
input = sys.stdin.readline

# 물품의 수, 버틸 수 있는 무게
N, K = map(int, input().split())

# 각 물건의 무게와 가치를 무게 기준으로 내림차순 정렬
items = sorted([list(map(int, input().split())) for _ in range(N)], reverse = True)

# 각 무게를 담았을 때의 최대 가치
value = defaultdict(int)
value[0] = 0

# 각 물건 탐색
for W, V in items:
    # value와 value에서 현재 물건을 담았을 때 비교
    temp = defaultdict(int)
    for i in value.copy().keys():
        w = W+i

        # 현재 물건을 담았을 때 최대 무게를 넘지 않는 경우
        # 현재 물건을 담지 않았을 때와 담았을 때의 무게 비교
        if not w > K:
            temp[w] = max(value[w], V + value[i])

    # update: 기존에 있는 값을 수정하고, 추가된 값은 추가
    value.update(temp)

print(max(value.values()))