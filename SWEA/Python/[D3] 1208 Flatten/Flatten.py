# 테스트 케이스
for t in range(1, 11):
    # 덤프 횟수
    limit = int(input())

    # 상자 높이
    H = list(map(int, input().split()))

    # 덤프할 수 있는 만큼 덤프
    while limit and max(H) - min(H) > 1:
        # 가장 높은 곳의 박스와 가장 낮은 곳의 박스의 위치
        mxi, mni = H.index(max(H)), H.index(min(H))

        # 덤프
        H[mxi] -= 1
        H[mni] += 1

        # 덤프 가능 횟수 감소
        limit -= 1

    print(f'#{t} {max(H) - min(H)}')