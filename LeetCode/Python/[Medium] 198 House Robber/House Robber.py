class Solution:
    def rob(self, nums: List[int]) -> int:
        # 집 수
        n = len(nums)

        # 집이 하나인 경우
        if n == 1:
            return nums[0]

        # money[0][i]: i번째 집을 도둑질하지 않았을 때의 돈의 최대값
        # money[1][i]: i번째 집을 도둑질했을 때의 돈의 최대값
        money = [[0] * n for _ in range(2)]
        money[1][0] = money[0][1] = nums[0]
        money[1][1] = nums[1]

        # 집 탐색
        for i in range(2, n):
            # 현재 집을 도둑질하는 경우
            # : 이전 집만 도둑질하지 않은 경우 or 두번째 전 집까지 도둑질하지 않은 경우
            money[1][i] = max(money[0][i - 1], money[0][i - 2]) + nums[i]

            # 현재 집을 도둑질하지 않는 경우
            # : 이전 집을 도둑질한 경우 or 두번째 전 집을 도둑질한 경우
            money[0][i] = max(money[1][i - 1], money[1][i - 2])

        return max(money[0][-1], money[1][-1])