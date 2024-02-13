from collections import deque
import sys
input = sys.stdin.readline

# 뿌요 터뜨리기
def remove():
    # 방문 체크
    visited = [[0] * 6 for _ in range(12)]

    # check[i]: i번째 열에서 터진 뿌요 중 가장 아래에 있는 뿌요의 행 번호
    check = [-1] * 6

    # 터뜨릴 뿌요 개수
    puyo = 0

    # 터뜨릴 뿌요 찾기
    for i in range(12):
        for j in range(6):
            # 뿌요가 있는 경우, 연결되어 있는 뿌요 확인
            if board[i][j] and not visited[i][j]:
                pos = [(i, j)]
                q = deque([(i, j)])
                visited[i][j] = 1
                while q:
                    r, c = q.popleft()
                    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if 0 <= nr < 12 and 0 <= nc < 6 and not visited[nr][nc] and board[nr][nc] == board[r][c]:
                            visited[nr][nc] = 1
                            q.append((nr, nc))
                            pos.append((nr, nc))

                # 뿌요가 4개 이상 모인 경우 터뜨리기
                if len(pos) >= 4:
                    puyo += len(pos)
                    for r, c in pos:
                        board[r][c] = 0
                        check[c] = max(check[c], r)

    # 터뜨린 뿌요 개수, 및 터진 뿌요의 열 반환
    return puyo, check

##################################################################################################################################

# 공중에 떠있는 뿌요 내리기
def down():
    # 터뜨린 뿌요가 있는 열 탐색
    for j in range(6):
        if check[j] != -1:
            r = check[j]
            # 밑에서부터 탐색
            for i in range(check[j] - 1, -1, -1):
                # 뿌요가 있는 경우 아래로 내리기
                if board[i][j]:
                    board[r][j] = board[i][j]
                    board[i][j] = 0
                    r -= 1

##################################################################################################################################

global check

# 필드 정보
board = [list(map(lambda x: {'.': 0, 'R': 1, 'G': 2, 'B': 3, 'P': 4, 'Y': 5}[x], input().rstrip())) for _ in range(12)]

# 연쇄 수
cnt = 0

# 연쇄가 없을 때까지 반복
while True:
    # 뿌요 터뜨리기
    # 터진 뿌요 개수, check 반환
    # check[i]: i번째 열에서 터진 뿌요 중 가장 아래에 있는 뿌요의 행 번호
    remove_cnt, check = remove()

    # 터진 뿌요가 없는 경우 끝내기
    if remove_cnt == 0:
        break
    cnt += 1

    # 뿌요 내리기
    down()

print(cnt)