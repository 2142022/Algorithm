import sys
input = sys.stdin.readline

# 시작점의 인덱스 구하기 by 이분 탐색
def get_start(num):

    global N
    
    left = 0
    right = N - 1

    while left <= right:
        mid = (left + right) // 2

        if num <= pos[mid]:
            right = mid - 1
        else:
            left = mid + 1
            
    return right + 1

# 끝점의 인덱스 구하기
def get_end(num):
    global N
    
    left = 0
    right = N - 1

    while left <= right:
        mid = (left + right) // 2

        if num < pos[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return right

# N: 점의 개수, M: 선분의 개수
N, M = map(int, input().split())

# 점의 좌표 오름차순 정렬
pos = list(map(int, input().split()))
pos.sort()

# M개의 선분
for i in range(M):
    # 선분의 시작과 끝
    start, end = map(int, input().split())

    # 시작점과 끝점의 인덱스 구하기
    start_idx = get_start(start)
    end_idx = get_end(end)

    print(end_idx - start_idx + 1)
