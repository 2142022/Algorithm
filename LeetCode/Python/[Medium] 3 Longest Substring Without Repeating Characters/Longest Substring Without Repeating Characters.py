class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 문자별 최근 인덱스
        idx = defaultdict(int)

        # 중복되는 문자가 없는 최대 문자열 길이, 탐색 중인 부분 문자열의 시작점
        l = start = 0

        # 문자 탐색
        for i, c in enumerate(s):
            # 현재 문자가 기존에 저장되어 있다면, 부분 문자열의 시작점 비교
            if c in idx:
                start = max(start, idx[c] + 1)

            # 현재 문자의 인덱스 갱신
            idx[c] = i

            # 최대 문자열 길이 갱신
            l = max(l, i - start + 1)
            
        return l