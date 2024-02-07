import sys
input = sys.stdin.readline

# 한 명씩 선택
# cnt: 뽑은 사람 수
# s: 임도연파 + 이다솜파
# path: 탐색 경로
def dfs(cnt, s, path):
    global result

    # 모든 사람을 뽑은 경우
    if cnt == 7:
        if s > 0:
            result += 1
        return

    # 나머지 다른 사람을 모두 이다솜파라고 해도 4명이 안 되는 경우 끝내기
    if 7 - cnt + s < 0:
        return

    # 이어질 수 있는 한 사람 선택하기
    for r, c in pos:
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if 0 <= nr < 5 and 0 <= nc < 5 and (nr, nc) not in pos and path | 1 << (5 * nr + nc) not in checked:
                pos.append((nr, nc))
                checked.add(path | 1 << (5 * nr + nc))
                dfs(cnt + 1, s + seat[nr][nc], path | 1 << (5 * nr + nc))
                pos.pop()

####################################################################################################################

# 자리 정보
seat = [list(map(lambda x : 1 if x == 'S' else -1, input().rstrip())) for _ in range(5)]

# 소문난 칠공주를 결성할 수 있는 가짓수
result = 0

# 탐색한 경로 체크
checked = set()

# 현재 조합의 위치
pos = []

# 한 명씩 선택
for i in range(5):
    for j in range(5):
        pos.append((i, j))
        checked.add(1 << (5 * i + j))
        dfs(1, seat[i][j], 1 << (5 * i + j))
        pos.pop()

print(result)