# 승자 구하기
def find_winner(start, end):
    # 1명인 경우 그대로 반환
    if start == end:
        return start

    # 좌우 그룹 나눠서 승자 구하기
    mid = (start + end) // 2
    left = find_winner(start, mid)
    right = find_winner(mid + 1, end)

    # 좌우 중 승자의 번호 구하기
    if cards[right] % 3 == (cards[left] + 1) % 3:
        return right
    else:
        return left

###################################################

# 테스트 케이스
for T in range(1, int(input()) + 1):
    # 인원
    N = int(input())

    # 각 사람이 고른 카드
    cards = [0] + list(map(int, input().split()))

    # 승자 구하기
    print(f'#{T} {find_winner(1, N)}')