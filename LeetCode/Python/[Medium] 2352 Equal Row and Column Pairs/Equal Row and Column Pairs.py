class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # 행렬의 크기
        n = len(grid)

        # grid의 행과 열을 바꾸기
        change = copy.deepcopy(grid)
        for i in range(n):
            for j in range(i + 1, n):
                grid[i][j], grid[j][i] = grid[j][i], grid[i][j]

        # 두 행렬의 같은 행의 개수
        cnt = 0
        
        # grid의 한 행씩 탐색
        for r1 in grid:
            # change의 한 행씩 탐색
            for r2 in change:
                if r1 == r2:
                    cnt += 1

        return cnt