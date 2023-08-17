class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 각 칸에 가는 경우의 수
        grid = [[1] * n for _ in range(m)]

        # 풀이: 현재 칸까지 가는 경우의 수 = 왼쪽 칸에 가는 경우의 수 + 위쪽 칸에 가는 경우의 수
        # 첫 행과 첫 열은 모두 1
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i - 1][j] + grid[i][j- 1]

        # 마지막 칸까지 가는 경우의 수 반환
        return grid[m - 1][n - 1]