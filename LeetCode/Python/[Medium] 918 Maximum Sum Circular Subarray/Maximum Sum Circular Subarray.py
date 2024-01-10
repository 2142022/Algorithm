class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # 배열의 총 합, 탐색 원소를 포함하는 최대 구간합, 탐색 원소를 포함하는 최소 구간합
        total = currMaxSum = currMinSum = 0
        # 최종 최대 구간합, 최종 최소 구간합 (최대 구간합 = 배열의 합 - 최소 구간합)
        maxSum, minSum = -sys.maxsize, sys.maxsize

        # 하나씩 탐색
        for n in nums:
            total += n
            currMaxSum = max(currMaxSum + n, n)
            currMinSum = min(currMinSum + n, n)
            maxSum = max(maxSum, currMaxSum)
            minSum = min(minSum, currMinSum)

        # 최대 구간합이 음수인 경우, 최소 구간합은 배열 전체가 됨 -> 최대 구간합이 0이 됨
        # 따라서, 최대 구간합이 음수인 경우에는 최대 구간합 반환
        if maxSum < 0:
            return maxSum
        else:
            return max(maxSum, total - minSum)