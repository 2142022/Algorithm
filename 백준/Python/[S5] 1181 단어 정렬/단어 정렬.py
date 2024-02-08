import sys
input = sys.stdin.readline

# 단어 개수
N = int(input())

# 길이 -> 사전 순으로 단어 정렬
words = sorted(list(set([input().rstrip() for _ in range(N)])), key = lambda x: (len(x), x))

# 출력
print(*words, sep='\n')