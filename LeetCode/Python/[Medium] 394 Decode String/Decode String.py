class Solution:
    def decodeString(self, s: str) -> str:
        # 스택에 담아놓기
        stack = []
        i = 0
        while i < len(s):
            # 숫자 담기
            num = ''
            while i < len(s) and '0' <= s[i] <= '9':
                num += s[i]
                i += 1
            if num:
                stack.append(int(num))
                continue

            # '[' 담기
            if s[i] == '[':
                stack.append('[')
                i += 1
                continue

            # 문자열 담기
            string = ''
            while i < len(s) and 'a' <= s[i] <= 'z':
                string += s[i]
                i += 1
            if string:
                # 스택에 문자열이 있었다면 합치기
                if stack and stack[-1] != '[' and type(stack[-1]) == str:
                    string = stack.pop() + string
                stack.append(string)
                continue

            # ']': '['가 나올 때까지 모두 꺼내고 앞의 숫자만큼 곱하기
            if s[i] == ']':
                string = stack.pop()
                stack.pop()
                string = stack.pop() * string

                # 앞에 더 합칠 문자열이 있는 경우 합치기
                if stack and stack[-1] != '[' and type(stack[-1]) == str:
                    string = stack.pop() + string
                stack.append(string)
                i += 1

        return ''.join(stack)
        