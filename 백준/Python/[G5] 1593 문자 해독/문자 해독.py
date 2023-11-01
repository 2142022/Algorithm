import sys
input = sys.stdin.readline

# W의 길이, S의 길이
g, s = map(int, input().split())

# 찾고자 하는 단어
W = input().rstrip()
# 벽화의 문자열
S = input().rstrip()

# W, S에서 각 알파벳의 개수 (A~Z, a~z)
wc = [0] * 52
sc = [0] * 52

# W의 알파벳 개수 세기
for i in W:
    if 'A' <= i <= 'Z':
        wc[ord(i) - ord('A')] += 1
    else:
        wc[ord(i) - ord('a') + 26] += 1

# W의 순열이 S 안에 있을 수 있는 형태의 개수
cnt = 0

# S[0] ~ S[g - 2]의 알파벳 개수 구하기
for i in range(g - 1):
    alpha = S[i]
    if 'A' <= alpha <= 'Z':
        sc[ord(alpha) - ord('A')] += 1
    else:
        sc[ord(alpha) - ord('a') + 26] += 1

# S[g - 1] ~ S[s - 1]의 알파벳 개수 구하기
for i in range(g - 1, s):
    alpha = S[i]
    if 'A' <= alpha <= 'Z':
        sc[ord(alpha) - ord('A')] += 1
    else:
        sc[ord(alpha) - ord('a') + 26] += 1

    # W의 순열로 만들 수 있는 경우
    if wc == sc:
        cnt += 1

    # g개씩 탐색하기 위해 S[i - g + 1]의 알파벳 개수 감소
    alpha = S[i - g + 1]
    if 'A' <= alpha <= 'Z':
        sc[ord(alpha) - ord('A')] -= 1
    else:
        sc[ord(alpha) - ord('a') + 26] -= 1

print(cnt)