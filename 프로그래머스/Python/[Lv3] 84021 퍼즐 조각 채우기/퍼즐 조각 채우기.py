from collections import defaultdict, deque

def solution(game_board, table):
    # 퍼즐 조각의 퍼즐 개수와 모양 찾기
    # sr, sc: 시작 위치
    # board: game_board 혹은 table
    # visited: 방문 체크
    # flag: game_board에서는 0, table에서는 1
    def get_shape(sr, sc, board, visited, flag):
        global N
        
        # 사방 탐색용
        dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
        
        # 퍼즐 조각의 모양 (시작 위치를 기준으로 상대적 위치 체크)
        shape = [(0, 0)]
        
        # 현재 위치를 담은 큐
        q = deque([(sr, sc)])
        while q:
            # 현재 위치
            r, c = q.popleft()
            
            # 사방 탐색
            for i in range(4):
                # 다음 위치
                nr, nc = r + dr[i], c + dc[i]
                
                # 범위를 벗어난 경우 패스
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                    
                # 퍼즐 조각이 아니거나 빈 칸이 아닌 경우 패스
                if board[nr][nc] != flag:
                    continue
                    
                # 방문 체크
                if visited & 1 << (N * nr + nc):
                    continue
                visited |= 1 << (N * nr + nc)
                
                # 퍼즐 조각의 모양 및 큐 갱신
                shape.append((nr - sr, nc - sc))
                q.append((nr, nc))
                
        return shape, visited
        
    ######################################################################
    
    global N
    
    # 보드 크기
    N = len(game_board)
    
    # 퍼즐 조각 (key: 퍼즐 조각의 개수, value: 퍼즐 조각 모양)
    block = defaultdict(list)
    # 퍼즐 조각용 방문체크
    block_visited = 0
    for i in range(N):
        for j in range(N):
            if table[i][j] == 1 and not block_visited & 1 << (N * i + j):
                block_visited |= 1 << (N * i + j)
                block_shape, block_visited = get_shape(i, j, table, block_visited, 1)
                block[len(block_shape)].append(block_shape)
                
    # 채울 수 있는 칸의 개수
    cnt = 0
    
    # 게임 보드 회전 횟수
    for k in range(4):
        # 처음을 제외하고 시계 방향으로 90도 회전
        if k != 0:
            game_board = list(map(list, zip(*game_board[::-1])))

        # 보드용 방문 체크
        board_visited = 0
        
        # 보드의 빈 칸 탐색
        for i in range(N):
            for j in range(N):
                if game_board[i][j] == 0 and not board_visited & 1 << (N * i + j):
                    board_visited |= 1 << (N * i + j)
                    empty_shape, board_visited = get_shape(i, j, game_board, board_visited, 0)
                    
                    # 빈 칸에 알맞는 퍼즐 조각이 있는 경우
                    if empty_shape in block[len(empty_shape)]:
                        cnt += len(empty_shape)
                        
                        # 빈 칸 막기
                        for r, c in empty_shape:
                            game_board[i + r][j + c] = 1
                            
                        # 퍼즐 사용
                        block[len(empty_shape)].remove(empty_shape)

    return cnt