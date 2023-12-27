class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # 행, 열 크기
        N, M = len(matrix), len(matrix[0])

        # 열별 1의 세로 길이
        # 마지막 열에서 항상 최대 사각형의 넓이를 비교하기 M + 1
        H = [0] * (M + 1)

        # 최대 사각형의 넓이
        area = 0

        # 행 탐색
        for i in range(N):
            # 세로 길이가 증가하도록 연속된 열의 인덱스를 저장한 스택
            stack = []

            # 열 탐색 (마지막 열에서 항상 최대 사각형의 넓이를 비교하기 M + 1까지 탐색)
            for j in range(M + 1):
                # 열별 1의 세로 길이 갱신
                if j < M:
                    if matrix[i][j] == '1':
                        H[j] += 1
                    else:
                        H[j] = 0

                # 이전 열보다 세로 길이가 작은 경우 최대 사각형 넓이 갱신
                while stack and H[j] < H[stack[-1]]:
                    # 이전 열의 세로 길이
                    h = H[stack.pop()]
                    # 연속된 열의 개수
                    if stack:
                        w = j - 1 - stack[-1]
                    else:
                        w = j
                    area = max(area, h * w)

                stack.append(j)

        return area