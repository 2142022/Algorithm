# 재료 하나씩 선택하기
# idx: 현재 재료
# score: 현재까지의 점수
# kcal: 현재까지의 칼로리
def select(idx, score, kcal):
    global max_score

    # 제한 칼로리를 넘어가는 경우 끝내기
    if kcal > K:
        return

    # 이미 제한 칼로리인 경우 끝내기
    if max_score == K:
        return

    # 모든 재료를 탐색한 경우 최대 점수 비교
    if idx == N:
        max_score = max(max_score, score)
        return

    # 현재 재료를 선택하는 경우
    select(idx + 1, score + ingre[idx][0], kcal + ingre[idx][1])
    # 현재 재료를 선택하지 않는 경우
    select(idx + 1, score, kcal)

########################################################################

# 테스트 케이스 수
T = int(input())
for t in range(1, T + 1):
    # 재료 수, 제한 칼로리
    N, K = map(int, input().split())

    # 재료에 대한 점수와 칼로리 (칼로리 기준 정렬)
    ingre = sorted([list(map(int, input().split())) for _ in range(N)], key = lambda x: x[1])

    # 가장 높은 점수
    max_score = 0

    # 재료 하나씩 선택하기
    select(0, 0, 0)

    print(f'#{t} {max_score}')