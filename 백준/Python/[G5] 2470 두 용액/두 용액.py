import sys
input = sys.stdin.readline

# 용액 수
N = int(input())

# 용액의 특성값 (오름차순 정렬)
value = sorted(list(map(int, input().split())))

# 가장 0에 가까운 용액의 특성값과 그 두 용액
min_diff, l1, l2 = value[0] + value[-1], value[0], value[-1]

# 두 용액의 특성값 구하기
left, right = 0, N - 1
while left < right:
    # 두 용액의 특성값
    s = value[left] + value[right]

    # 0이라면 끝내기
    if s == 0:
        l1 = value[left]
        l2 = value[right]
        break

    # 0에 가까운 특성값과 비교
    if abs(s) < abs(min_diff):
        min_diff = s
        l1 = value[left]
        l2 = value[right]

    # 현재 특성값이 양수라면 오른쪽 인덱스를, 음수라면 왼쪽 인덱스를 이동
    if s < 0:
        left += 1
    else:
        right -= 1

print(l1, l2)
