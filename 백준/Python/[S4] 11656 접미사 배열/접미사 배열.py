import sys
input = sys.stdin.readline

# 문자열 배열
S = input().rstrip()

# 모든 접미사
result = []
for i in range(len(S)):
    result.append(S[i:])

# 사전순으로 정렬 (오름차순 정렬)
result.sort()

# 모든 접미사 출력
for s in result:
    print(s)