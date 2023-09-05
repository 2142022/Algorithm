import sys
from collections import deque

# (r1, c1)에서 (r2, c2)까지 이동하는 최소 횟수 반환
def get_cnt(r1, c1, r2, c2, board):
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)
    
    q = deque([(0, r1, c1)])
    
    while q:
        cnt, r, c = q.popleft()
        
        # enter 입력까지 포함하기 위해 +1
        if r == r2 and c == c2:
            return cnt + 1
        
        # 사방 탐색 + 그 방향에 있는 가장 가까운 카드 탐색
        for i in range(4):
            nr, nc = r, c
            
            while True:
                nr += dr[i]
                nc += dc[i]
            
                if not (0 <= nr <= 3 and 0 <= nc <= 3):
                    break
                    
                # ctrl + 방향키로 다음 카드까지 이동하거나 이동 방향의 끝인 경우
                if board[nr][nc] or not (0 <= nr + dr[i] <= 3 and 0 <= nc + dc[i] <= 3):
                    q.append((cnt + 1, nr, nc))
                    break
                    
                # 한 칸 이동
                if nr == r + dr[i] and nc == c + dc[i]:
                    q.append((cnt + 1, nr, nc))
                    
##################################################################################################

# 현재 위치에서 카드 2개를 제거하기 위해 이동하는 횟수 구하기
# 카드1을 먼저 제거하는 경우, 카드2를 먼저 제거하는 경우 모두 반환
# (r, c): 현재 위치
# (r1, c1), (r2, c2): 제거할 카드 위치
# board: 현재 보드 상태
def get_total_cnt(r, c, r1, c1, r2, c2, board):
    cnt1 = get_cnt(r, c, r1, c1, board)
    cnt2 = get_cnt(r, c, r2, c2, board)
    
    # (r1, c1) -> (r2, c2)의 경로와 (r2, c2) -> (r1, c1)의 경로가 다를 수 있음
    cnt3 = get_cnt(r1, c1, r2, c2, board)
    cnt4 = get_cnt(r2, c2, r1, c1, board)
    
    return [(r1, c1, cnt2 + cnt4), (r2, c2, cnt1 + cnt3)]

##################################################################################################

# DFS로 모든 카드 제거
# (r, c): 현재 위치
# shift_cnt: 이동 횟수
# remove_cnt: 제거한 카드의 개수
# removed: 제거한 카드 체크
# board: 현재 보드 상태
def dfs(r, c, shift_cnt, remove_cnt, removed, board):
    global card_cnt, min_cnt, cards

    # 모든 카드를 제거한 경우 끝내기
    if remove_cnt == card_cnt:
        min_cnt = min(min_cnt, shift_cnt)
        return

    # 이미 이동 횟수가 min_cnt보다 크다면 끝내기
    if shift_cnt >= min_cnt:
        return

    # 카드 하나 제거하기
    for i in range(1, card_cnt + 1):
        # 이미 제거한 카드 패스
        if removed[i]:
            continue

        # 제거할 2개의 카드 위치
        (r1, c1), (r2, c2) = cards[i]
        
        # 카드 2개를 제거하는 2가지 경우 (카드1 먼저 제거 or 카드2 먼저 제거)
        (nr1, nc1, cnt1), (nr2, nc2, cnt2) = get_total_cnt(r, c, r1, c1, r2, c2, board)
        removed[i] = 1
        board[r1][c1] = board[r2][c2] = 0
        
        # 다음 카드 제거
        dfs(nr1, nc1, shift_cnt + cnt1, remove_cnt + 1, removed, board)
        dfs(nr2, nc2, shift_cnt + cnt2, remove_cnt + 1, removed, board)
        
        # 현재 카드 복구
        removed[i] = 0
        board[r1][c1] = board[r2][c2] = i

##################################################################################################

def solution(board, r, c):
    global card_cnt, min_cnt, cards
    
    # 서로 다른 카드의 개수
    card_cnt = 0
    # 서로 다른 카드의 위치
    cards = [[] for _ in range(9)]
    for i in range(4):
        for j in range(4):
            idx = board[i][j]
            if idx:
                cards[idx].append((i, j))
                if len(cards[idx]) == 2:
                    card_cnt += 1

    # 모든 카드를 제거하기 위한 키 조작 횟수의 최솟값
    min_cnt = sys.maxsize

    # DFS로 모든 카드 제거
    dfs(r, c, 0, 0, [0] * (card_cnt + 1), board)

    return min_cnt