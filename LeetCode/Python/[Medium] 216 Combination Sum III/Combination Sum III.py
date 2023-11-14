class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # 합이 n이 되는 조합
        result = []

        # 모든 조합 탐색
        for nums in combinations(range(1, 10), k):
            # 합이 n이 되면 결과 갱신
            if sum(nums) == n:
                result.append(list(nums))

        return result