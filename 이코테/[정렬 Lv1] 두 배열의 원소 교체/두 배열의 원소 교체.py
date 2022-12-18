import sys
input = sys.stdin.readline

# N: 각 배열의 원소의 개수, K: 최대 바꿔치기 연산 수
N, K = map(int, input().split())

# 배열 A, B
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A는 오름차순 정렬, B는 내림차순 정렬
A.sort()
B.sort(reverse=True)

# 최대 K번 바꿔치기 연산 수행
for i in range(K):
    # B의 최댓값이 A의 최솟값보다 크다면 바꾸기
    if B[i] > A[i]:
        A[i], B[i] = B[i], A[i]
    # 아니라면 더 이상 바꿀 필요 없으므로 끝내기
    else:
        break

# 배열 A의 원소의 합 출력
print(sum(A))