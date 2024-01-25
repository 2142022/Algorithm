# 10개의 테스트케이스
for t in range(1, 11):
    # 회문의 길이
    N = int(input())

    # 글자판
    board = [input().rstrip() for _ in range(8)]

    # 회문 개수
    cnt = 0

    # 시작 행 / 열
    for i in range(8):
        # 시작 열 / 행
        for j in range(9 - N):
            # 가로 회문
            if board[i][j:j + N] == board[i][j:j + N][::-1]:
                cnt += 1

            # 세로 회문
            if list(zip(*board[j:j + N]))[i] == list(zip(*board[j:j + N][::-1]))[i]:
                cnt += 1

    print(f'#{t} {cnt}')