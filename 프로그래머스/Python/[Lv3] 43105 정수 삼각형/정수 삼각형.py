def solution(triangle):
    # 두 번째 줄부터 탐색
    for i in range(1, len(triangle)):
        # 각 줄의 왼쪽부터 탐색
        for j in range(i + 1):
            # 왼쪽 상단, 오른쪽 상단까지의 경로 합
            left = right = 0
            if j > 0:
                left = triangle[i - 1][j - 1]
            if j < i:
                right = triangle[i - 1][j]
                
            # 왼쪽 상단과 오른쪽 상단을 비교하여 현재 위치까지의 합 갱신
            triangle[i][j] += max(left, right)
    
    return max(triangle[-1])