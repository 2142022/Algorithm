import sys
input = sys.stdin.readline

# 문서
docs = input().rstrip()

# 검색 단어
find = input().rstrip()

# 검색 단어의 길이
l = len(find)

# 검색 단어가 나오는 횟수
cnt = 0

# 문서 탐색
i = 0
while i <= len(docs) - l:
    # 문서와 검색 단어의 글자가 일치하는 경우
    if docs[i:i + l] == find:
        cnt += 1
        i += l
    else:
        i += 1

print(cnt)