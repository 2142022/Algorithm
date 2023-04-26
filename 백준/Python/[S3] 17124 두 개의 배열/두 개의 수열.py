from bisect import bisect_left
import sys
input = sys.stdin.readline

# 테스트 케이스 개수
T = int(input())

# T개의 테스트케이스
for _ in range(T):
    # n: A의 원소의 개수, m: B의 원소의 개수
    n, m = map(int, input().split())

    # A, B 입력받기
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # B를 오름차순 정렬
    B.sort()

    # 배열 C의 원소의 합
    result = 0

    # A의 원소 하나씩 탐색
    for a in A:
        # 이진 탐색을 했을 때, a가 들어갈 수 있는 인덱스
        idx = bisect_left(B, a)

        # 맨 처음에 넣을 수 있는 경우, B의 첫 번째 원소 더하기
        if idx == 0:
            result += B[idx]
        # 마지막에 넣을 수 있는 경우, B의 마지막 원소 더하기
        elif idx == m:
            result += B[idx - 1]
        # 그 외는 왼쪽과 오른쪽 수 중 더 가까운 수 더하기
        else:
            if abs(a - B[idx]) < abs(a - B[idx - 1]):
                result += B[idx]
            else:
                result += B[idx - 1]

    print(result)