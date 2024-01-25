# 가로, 세로 확인 함수
def line():
    for i in range(9):
        # 가로 확인 (i행)
        if len(set(puzzle[i])) != 9:
            return 0

        # 세로 확인 (i열)
        if len(set([r[i] for r in puzzle])) != 9:
            return 0

    return 1

#########################################################################

# 3 X 3 확인
def square():
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            num = set()
            for r in range(i, i + 3):
                for c in range(j, j + 3):
                    if puzzle[r][c] in num:
                        return 0
                    num.add(puzzle[r][c])

    return 1

#########################################################################

# 테스트케이스 개수
T = int(input())
for t in range(1, T + 1):
    # 퍼즐
    puzzle = [list(map(int, input().split())) for _ in range(9)]

    # 가로, 세로, 3X3 확인
    if line() and square():
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')

