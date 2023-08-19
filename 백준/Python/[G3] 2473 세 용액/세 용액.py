from itertools import combinations
import sys
input = sys.stdin.readline

# 용액의 수
N = int(input())

# 각 용액의 특성값
liquid = list(map(int, input().split()))
# 오름차순 정렬
liquid.sort()

# 세 용액(인덱스 a, b, c)를 혼합했을 때 가장 0에 가까운 특성값 m
m = 3000000000
a = b = c = -1

# i: 특성값이 가장 작은 용액의 인덱스
for i in range(N - 2):
    # 특성값이 중간인 용액의 인덱스
    left = i + 1
    # 특성값이 가장 큰 용액의 인덱스
    right = N - 1

    # 혼합 용액의 특성값이 0이 되었는지 확인용 변수
    finish = False

    # 모든 용액을 탐색할 때까지 반복
    while left < right:
        # 현재 혼합 용액의 특성값
        mix = liquid[i] + liquid[left] + liquid[right]

        # 기존 혼합 용액보다 0에 더 가까운 경우 갱신
        if abs(mix) < m:
            m = abs(mix)
            a = i
            b = left
            c = right

        # 혼합 용액의 특성값이 0이 되었다면 끝내기
        if mix == 0:
            finish = True
            break
        # 혼합 용액의 특성값이 양수라면 오른쪽 용액의 특성값 줄이기
        elif mix > 0:
            right -= 1
        # 혼합 용액의 특성값이 음수라면 왼쪽 용액의 특성값 줄이기
        else:
            left += 1

    # 혼합 용액의 특성값이 0이 되었다면 끝내기
    if finish:
        break

# 세 용액 출력
print(liquid[a], liquid[b], liquid[c])
