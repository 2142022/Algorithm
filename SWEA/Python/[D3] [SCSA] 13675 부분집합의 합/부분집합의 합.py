# 숫자 num까지 탐색했을 때의 합 sum
# cnt: 선택한 숫자의 개수
def dfs(num, sum, cnt):
    global N, K, result

    # N개의 합이 K가 된 경우
    if cnt == N and sum == K:
        result += 1
        return

    # 합이 K를 초과하거나 선택한 숫자가 N을 초과한 경우 끝내기
    if sum > K or cnt > N:
        return

    # 모든 숫자를 다 탐색한 경우 끝내기
    if num == 13:
        return

    # 나머지 숫자를 다 더해도 N개 미만이거나 K 미만인 경우
    if 13 - num + cnt < N or sum + (12 + num) * (13 - num) // 2 < K:
        return

    # 현재 숫자를 더하는 경우
    dfs(num + 1, sum + num, cnt + 1)

    # 현재 숫자를 더하지 않는 경우
    dfs(num + 1, sum, cnt)

######################################################################

# 테스트 케이스 수
T = int(input())
for t in range(1, T + 1):
    # 부분 집합의 원소 수, 부분 집합의 합
    N, K = map(int, input().split())

    # N개의 합이 K가 되는 경우의 수
    result = 0

    # 숫자 하나씩 선택
    dfs(1, 0, 0)

    print(f'#{t} {result}')