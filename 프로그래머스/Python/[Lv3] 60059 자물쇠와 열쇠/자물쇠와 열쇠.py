# https://school.programmers.co.kr/learn/courses/30/lessons/60059

# 열쇠 회전시키기
# 열쇠 한 변의 길이
# n = 0: 열쇠 90도 회전
# n = 1: 열쇠 180도 회전
# n = 2: 열쇠 270도 회전
def change(key, M, n):
    # 회전한 열쇠
    result = [[0] * M for i in range(M)]

    for i in range(M):
        for j in range(M):
            # 90도 회전
            if n == 0:
                result[j][M - 1 - i] = key[i][j]

            # 180도 회전
            elif n == 1:
                result[M - 1 - i][M - 1 - j] = key[i][j]

            # 270도 회전
            elif n == 2:
                result[M - 1 - j][i] = key[i][j]

    return result


# 열쇠와 자물쇠 비교하기
# M: 열쇠 한 변의 크기
# r, c: 현재 보드의 위치
# cnt: 자물쇠의 홈 개수
def check(key, board, M, r, c, cnt):
    for i in range(M):
        for j in range(M):
            # 열쇠의 돌기와 자물쇠의 홈이 일치하는 경우
            if board[r + i][c + j] == 0 and key[i][j] == 1:
                cnt -= 1

            # 자물쇠의 돌기와 열쇠의 돌기가 만난다면 무조건 False
            elif board[r + i][c + j] == 1 and key[i][j] == 1:
                return False

    # 자물쇠의 모든 홈이 채워진 경우
    if cnt == 0:
        return True

    return False


def solution(key, lock):
    # 열쇠 한 변의 크기
    M = len(key)

    # 자물쇠 함 변의 크기
    N = len(lock)

    # 한 변의 크기가 (M-1) + N + (M-1)인 보드 만들기
    # 자물쇠의 홈과 자물쇠가 아닌 부분을 구분하기 위해서 -1로 초기화하기
    board = [[-1] * (2 * M + N - 2) for i in range(2 * M + N - 2)]

    # 자물쇠의 홈 개수
    cnt = 0

    # 보드의 중앙을 자물쇠와 일치하게 만들기
    for i in range(N):
        for j in range(N):
            board[i + M - 1][j + M - 1] = lock[i][j]

            if lock[i][j] == 0:
                cnt += 1

    # 자물쇠의 홈이 없다면 열려있는 것으로, 항상 True
    if cnt == 0:
        return True

    # 한 칸씩 자물쇠와 열쇠 비교하기
    for i in range(M + N - 1):
        for j in range(M + N - 1):
            # 열쇠와 자물쇠 비교하기
            if check(key, board, M, i, j, cnt):
                return True

            # 열쇠를 회전한 후, 자물쇠와 비교하기
            for k in range(3):
                # 자물쇠를 열 수 있다면 true 반환
                if check(change(key, M, k), board, M, i, j, cnt):
                    return True

    return False
