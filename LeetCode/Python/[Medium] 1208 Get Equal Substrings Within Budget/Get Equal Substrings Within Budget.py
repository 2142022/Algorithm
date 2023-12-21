class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # 문자열의 길이
        N = len(s)

        # 부분 문자열의 시작 인덱스
        start = 0

        # 최종적으로 필요한 비용
        total = 0

        # 부분 문자열의 최대 길이
        length = 0

        # 각 문자를 바꾸는데 필요한 비용
        cost = [0] * N

        # 한 글자씩 탐색
        for i in range(N):
            # 현재 글자를 바꾸는데 필요한 비용 갱신
            c = abs(ord(s[i]) - ord(t[i]))
            cost[i] = c

            # 현재까지의 비용 갱신
            total += c
            
            # 현재까지의 비용이 maxCost 이하인 경우 부분 문자열의 최대 길이 갱신
            if total <= maxCost:
                length = max(length, i - start + 1)
            # 현재까지의 비용이 maxCost를 벗어난 경우, 앞에서부터 부분 문자열을 줄이기
            else:
                while total > maxCost:
                    total -= cost[start]
                    start += 1

        return length
