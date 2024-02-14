import sys
input = sys.stdin.readline

# 원판 옮기기
# cnt: 옮겨야 하는 원판의 개수
# before: 현재 장대 번호
# after: 이동해야 하는 장대 번호
# other: befor, after 외 나머지 장대
def shift(cnt, before, after, other):
    # 이동해야 하는 원판의 개수가 1개인 경우
    if cnt == 1:
        print(before, after)
        return

    # 현재 옮겨야 하는 원판들 중 맨 아래를 제외한 나머지 원판들을 other로 옮겨놓기
    shift(cnt - 1, before, other, after)

    # 맨 아래 원판을 after로 옮기기
    shift(1, before, after, other)

    # 나머지 원판들을 after로 옮기기
    shift(cnt - 1, other, after, before)

########################################################################################

# 원판 개수
N = int(input())

# 원판 옮긴 횟수: 2 ** (원판의 개수) - 1
print(2 ** N - 1)

# 원판 옮기기
shift(N, 1, 3, 2)