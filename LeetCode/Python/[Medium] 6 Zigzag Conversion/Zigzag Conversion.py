class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # numRows가 1인 경우 그대로 반환
        if numRows == 1:
            return s

        # 각 행별 문자열
        rows = [list() for _ in range(numRows)]

        # 탐색 문자가 들어갈 행, 진행 방향
        i , d = 0, -1
        for c in s:
            rows[i].append(c)
            
            # 첫 행이나 마지막 행인 경우, 진행 방향 바꾸기
            if i == 0 or i == numRows - 1:
                d *= -1
            
            i += d

        # 모든 문자열 합친 결과
        result = ''
        for i in rows:
            result += ''.join(i)

        return result

        