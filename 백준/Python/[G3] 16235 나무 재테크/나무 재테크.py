from collections import defaultdict
import sys
input = sys.stdin.readline

# 봄: 자신의 나이만큼 양분 먹고, 나이 증가
# 여름: 양분을 먹지 못한 나무 소멸
def spring_summer():
    global M

    # 나무 위치
    for k, v in list(trees.items()):
        r, c = divmod(k, N)
        total = len(v)

        # 현재 칸에 있는 모든 나무들의 번호
        i = 0
        while i < total:
            age = v[i]

            # 자신의 나이만큼 양분 먹고 나이 증가
            if ground[r][c] >= age:
                ground[r][c] -= age
                v[i] += 1

                # 나이가 5의 배수가 된 경우 가을에 번식
                if (age + 1) % 5 == 0:
                    year5[k] += 1

            # 양분이 없다면 나머지 나무들은 양분을 먹을 수 없으므로 소멸
            else:
                break
            i += 1

        # 양분을 못 먹은 나무들 소멸 -> 양분이 됨
        if i < total:
            ground[r][c] += sum(list(map(lambda x: x // 2, v[i:])))
            M -= total - i

            # 그 칸에 더 이상 나무가 없는 경우
            if i == 0:
                trees.pop(k)
            else:
                trees[k] = v[:i]

############################################################################################################################################################

# 가을: 나이가 5의 배수인 나무 번식
# 겨울: 양분 추가
def fall_winter():
    global M

    for r in range(N):
        for c in range(N):
            # 현재 칸에서 나이가 5의 배수인 나무들의 개수
            k = N * r + c
            if k in year5:
                cnt = year5[k]

                # 번식할 위치
                for nr, nc in ((r - 1, c - 1), (r - 1, c), (r - 1, c + 1), (r, c - 1), (r, c + 1), (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)):
                    # 범위 체크
                    if not (0 <= nr < N and 0 <= nc < N):
                        continue

                    # 나무 추가 (어린 나무부터 양분을 먹어야 하므로 앞에 추가)
                    M += cnt
                    nk = N * nr + nc
                    for _ in range(cnt):
                        trees[nk].insert(0, 1)

            # 양분 추가
            ground[r][c] += A[r][c]

############################################################################################################################################################

# 땅 크기, 나무 수, K년 후 결과 구하기
N, M, K = map(int, input().split())

# 매년 추가할 양분
A = [list(map(int, input().split())) for _ in range(N)]

# 땅의 양분
ground = [[5] * N for _ in range(N)]

# 각 위치에 있는 나무의 나이
trees = defaultdict(list)
for _ in range(M):
    # 나무 위치, 나이
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    trees[N * x + y].append(z)

# K년 동안 반복
for _ in range(K):
    # 각 칸에서 나이가 5의 배수가 된 나무의 개수와 소멸된 나무 구하기
    year5 = defaultdict(int)
    spring_summer()

    # 나이가 5의 배수인 나무 번식 & 양분 추가
    fall_winter()

# 살아남은 나무 수
print(M)