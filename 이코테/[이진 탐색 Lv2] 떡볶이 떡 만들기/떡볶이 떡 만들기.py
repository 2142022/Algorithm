import sys
input = sys.stdin.readline

# N: 떡의 개수, M: 떡의 길이
N, M = map(int, input().split())

# N개의 떡의 길이
rice_cake = list(map(int, input().split()))

# 절단기 높이의 최댓값
H = 0

# 이진 탐색을 통해 절단기 높이의 최댓값 찾기
start = 0
end = max(rice_cake)
while start <= end:
    mid = (start + end) // 2

    # 남은 떡 길이
    rest = 0

    # 남은 떡 길이 계산하기
    for i in rice_cake:
        # 떡이 절단기보다 큰 경우에만 더하기
        if i > mid:
            rest += i - mid

    # 남은 떡의 길이가 손님이 요청한 떡의 길이와 같다면 끝내기
    if rest == M:
        H = mid
        break
    # 남은 떡의 길이가 손님이 요청한 떡의 길이보다 작다면 end 낮추기
    elif rest < M:
        end = mid - 1
    # 남은 떡의 길이가 손님이 요청한 떡의 길이보다 크다면 start 높이기
    else:
        # 절단기 높이의 최댓값일 수 있으므로 mid 저장해두기
        H = mid
        start = mid + 1

print(H)