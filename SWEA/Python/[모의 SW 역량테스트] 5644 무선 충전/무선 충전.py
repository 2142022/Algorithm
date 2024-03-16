# 현재 위치에서 충전하기
def charge():
    # A, B가 사용할 수 있는 충전기의 충전량과 번호
    a = [(p, i) for i, c, r, l, p in BC if abs(r - ar) + abs(c - ac) <= l]
    b = [(p, i) for i, c, r, l, p in BC if abs(r - br) + abs(c - bc) <= l]

    # 두 사람이 충전 범위 내에 있는 경우
    if a and b:
        # 두 사람이 다른 충전기를 사용하는 경우
        if a[0][1] != b[0][1]: return a[0][0] + b[0][0]
        # 두 사람이 같은 충전기를 사용하는 경우
        res = a[0][0]
        if len(a) > 1: res = max(res, a[1][0] + b[0][0])
        if len(b) > 1: res = max(res, a[0][0] + b[1][0])
        return res
    # 한 사람은 충전 범위가 아닌 경우
    elif a: return a[0][0]
    elif b: return b[0][0]
    # 두 사람 모두 충전 범위가 아닌 경우
    else: return 0

################################################################################################

# 사방 탐색
dr, dc = (0, -1, 0, 1, 0), (0, 0, 1, 0, -1)

# 테스트 케이스
for TC in range(1, int(input()) + 1):
    # 이동 시간, 충전기 개수
    T, N = map(int, input().split())

    # 사용자 A, B의 이동 정보
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 충전기 정보 (충전량 기준 내림차순 정렬)
    BC = sorted([[i] + list(map(int, input().split())) for i in range(N)], key=lambda x: -x[4])

    # 사용자 A, B의 위치
    ar, ac = 1, 1
    br, bc = 10, 10

    # 모든 사용자의 최대 충전량 합
    total = charge()

    # 사용자 이동
    for i in range(T):
        # 사용자들의 이동 방향
        ad, bd = A[i], B[i]

        # 이동
        ar += dr[ad]
        ac += dc[ad]
        br += dr[bd]
        bc += dc[bd]

        # 현재 위치에서 충전하기
        total += charge()

    print(f'#{TC} {total}')
