import sys
input = sys.stdin.readline

# 좋은 단어 수
cnt = 0

# 한 단어씩 탐색
for _ in range(int(input())):
    # 단어
    word = input().rstrip()

    # 짝이 이어지지 않은 알파벳을 저장한 스택
    stack = []
    for c in word:
        # 이전 알파벳과 동일하면 짝이므로 제거
        if stack and c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)

    # 모든 알파벳이 제거된 경우, 좋은 단어
    if not stack:
        cnt += 1

print(cnt)