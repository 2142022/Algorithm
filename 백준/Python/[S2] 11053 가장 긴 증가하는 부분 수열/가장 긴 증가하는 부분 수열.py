import sys
input = sys.stdin.readline

# 수열의 크기
N = int(input())

# 수열
A = list(map(int, input().split()))

# 증가하는 부분 수열 길이를 나타내는 배열
length = [1] * N

for i in range(N):
    for j in range(i + 1, N):
        # 증가한다면
        if A[j] > A[i]:
            # 기존에 저장된 길이보다 작다면
            if length[j] < length[i] + 1:
                # 길이 증가시키기
                length[j] = length[i] + 1

print(max(length))
