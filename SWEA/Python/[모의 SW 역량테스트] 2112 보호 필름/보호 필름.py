from itertools import combinations, product

# 합격 여부 확인
def check(board):
    # 문자열로 바꾸고 한 줄씩 확인
    for b in board:
        temp = ''.join(b)
        # K개 이상 연속되지 않는 경우
        if '0' * K not in temp and '1' * K not in temp:
            return 0
    return 1

###################################################################################################################

# 약품 투입 횟수 구하기
def get_cnt(board):
    # 약품 투입 횟수
    for cnt in range(1, K):
        # 약품 투입 위치
        combs = tuple(combinations(range(D), cnt))

        # 각 위치에 바꿀 특성
        prods = tuple(product(['0', '1'], repeat = cnt))

        # 조합
        for pos in combs:
            # 각 위치에 바꿀 특성
            for nums in prods:
                # 약품 투입 결과
                result = [b[:] for b in board]
                for j, num in zip(pos, nums):
                    for i in range(W):
                        result[i][j] = num

                # 합격 여부 확인
                if check(result):
                    return cnt

    # K번 다 바꾸기
    return K

###################################################################################################################

# 테스트 케이스
for TC in range(1, int(input()) + 1):
    # 보호 필름 두께, 가로 크기, 합격 기준
    D, W, K = map(int, input().split())

    # 보호 필름 (90도 회전)
    board = list(map(list, zip(*[list(input().split()) for _ in range(D)][::-1])))

    # 합격
    if check(board):
        print(f'#{TC} 0')

    # 약품 투입 횟수
    else:
        print(f'#{TC} {get_cnt(board)}')

