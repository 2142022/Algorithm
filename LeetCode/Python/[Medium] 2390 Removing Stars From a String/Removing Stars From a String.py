class Solution:
    def removeStars(self, s: str) -> str:
        # 스택에 문자 하나씩 담기
        # *은 마지막 원소 pop
        stack = []
        for c in s:
            if c == '*':
                stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)