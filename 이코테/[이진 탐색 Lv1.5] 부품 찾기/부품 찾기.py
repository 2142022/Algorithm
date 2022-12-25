import sys
input = sys.stdin.readline

# 이진 탐색을 이용하여 재고가 있는지 확인
def is_exist(part):
    global N
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2

        # 재고가 있으면 True 반환
        if part == stock[mid]:
            return True
        # 현재 부품의 번호보다 작다면 이전 부품만 탐색
        elif part < stock[mid]:
            end = mid - 1
        # 현재 부품의 번호보다 크다면 이후 부품만 탐색
        else:
            start = mid + 1

    # 모두 탐색했는데 재고가 없다면 False 반환
    return False

###################################################

# 전자 매장에 있는 부품의 개수
N = int(input())

# 전자 매장에 있는 부품
stock = list(map(int, input().split()))

# 오름차순 정렬
stock.sort()

# 손님이 문의한 부품의 개수
M = int(input())

# 손님이 문의한 부품
ask = list(map(int, input().split()))

# 손님이 문의한 부품마다 재고가 있는지 확인
for i in ask:
    # 이진 탐색을 이용하여 확인
    if is_exist(i):
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
