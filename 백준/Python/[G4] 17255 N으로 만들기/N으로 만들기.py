import sys
input = sys.stdin.readline

# 재귀함수를 이용하여 경로 구하기
# x: 처음 숫자의 위치, y: 마지막 숫자의 위치
# route: 현재까지의 경로
# ex) 1 -> 11 -> 111 -> 9111의 최종 route는 1111119111
def dfs(x, y, route):
    global l

    # N을 구하면 그만두기
    if x == 0 and y == l - 1:
        case.add(route)
        return

    # 왼쪽에 숫자 두기
    if x - 1 >= 0:
        dfs(x - 1, y, route + N[x - 1] + route)

    # 오른쪽에 숫자 두기
    if y + 1 < l:
        dfs(x, y + 1, 2 * route + N[y + 1])

# 만들 수
N = input().rstrip()

# N의 자릿수
l = len(N)

# 모든 경로
case = set()

# 한 숫자씩 출발 숫자로 지정
for i in range(l):
    # i번째 숫자로 시작했을 때의 모든 경우 찾기
    dfs(i, i, N[i])

print(len(case))