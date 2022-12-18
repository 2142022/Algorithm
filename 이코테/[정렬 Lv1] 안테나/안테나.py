import sys
input = sys.stdin.readline

# 집의 수
N = int(input())

# 집의 위치를 나타내는 배열
home = list(map(int, input().split()))

# 집의 위치를 오름차순 정렬
home.sort()

# 안테나를 설치할 집은 중간에 있는 집
# 집의 수가 짝수라면 중간에 있는 두 집 어디에 설치해도 똑같음
print(home[(N - 1) // 2])