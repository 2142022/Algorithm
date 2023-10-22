class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 최대 공통 문자열의 개수
        cnt = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]

        # text2 탐색
        for i in range(1, len(text2) + 1):
            # text1 탐색
            for j in range(1, len(text1) + 1):
                # text1과 text2가 동일한 부분
                if text2[i - 1] == text1[j - 1]:
                    cnt[i][j] = cnt[i - 1][j - 1] + 1

                # 다르다면 기존 cnt의 최대값 저장
                else:
                    cnt[i][j] = max(cnt[i - 1][j], cnt[i][j - 1])

        return cnt[-1][-1]