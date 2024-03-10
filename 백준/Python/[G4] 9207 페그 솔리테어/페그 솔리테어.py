import sys
input = sys.stdin.readline

# 핀 하나씩 옮기기
# cnt: 남아있는 핀의 개수
def move(cnt):
    global min_cnt

    # 핀이 1개 남은 경우 끝
    if cnt == 1:
        min_cnt = 1
        return 1

    # 핀
    for r in range(N):
        for c in range(M):
            if board[r][c] == 1:
                # 사방 탐색
                for d in range(4):
                    nr, nc = r + dc[d], c + dr[d]
                    nnr, nnc = nr + dc[d], nc + dr[d]

                    # 범위 체크
                    if not (0 <= nnr < N and 0 <= nnc < M):
                        continue

                    # 다음 칸에 핀이 있고 다다음 칸이 비어있는 경우 이동
                    if board[nr][nc] == 1 and board[nnr][nnc] == 0:
                        board[r][c] = 0
                        board[nr][nc] = 0
                        board[nnr][nnc] = 1
                        if move(cnt - 1):
                            return 1
                        else:
                            min_cnt = min(min_cnt, cnt - 1)
                        # 초기화
                        board[r][c] = 1
                        board[nr][nc] = 1
                        board[nnr][nnc] = 0

    return 0

#################################################################################

# 게임판 크기
N, M = 5, 9

# 사방 탐색용
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

# 테스트 케이스
TC = int(input())
for tc in range(TC):
    # 게임판
    board = []
    # 핀 개수
    total = 0
    for _ in range(N):
        row = list(map(lambda x: {'#': -1, '.': 0, 'o': 1}[x], input().rstrip()))
        board.append(row)
        for j, info in enumerate(row):
            if info == 1:
                total += 1

    # 남긴 핀의 최소 개수
    min_cnt = total

    # 핀 하나씩 옮기기
    move(total)

    # 남길 수 있는 핀의 최소 개수와 그 개수를 만들기 위해 필요한 최소 이동 횟수
    print(min_cnt, total - min_cnt)

    if tc < TC - 1:
        input()