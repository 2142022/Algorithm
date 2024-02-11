import sys
input = sys.stdin.readline

# 직사각형 가로 크기
n = int(input())

# n이 1인 경우
if n == 1:
    print(1)
    exit()

# 각 열까지 채웠을 때의 경우의 수
cnt = [0] * n
cnt[0] = 1
cnt[1] = 2
for i in range(2, n):
    # 이전 열에서 2 X 1 타일 붙이는 방법
    # + 두번째 전 열에서 1 X 2 타일 2개를 붙이는 방법
    cnt[i] = (cnt[i - 1] + cnt[i - 2]) % 10007

print(cnt[n - 1])