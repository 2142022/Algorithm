class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # 수의 개수
        n = len(nums)

        # 왼쪽 수들의 합
        left = 0
        # 오른쪽 수들의 합
        right = sum(nums)

        # 하나씩 탐색
        for i in range(n):
            right -= nums[i]
            
            # 왼쪽과 오른쪽이 같다면 피벗 인덱스
            if left == right:
                return i
            
            left += nums[i]

        # 모두 탐색했을 때 피벗 인덱스가 없다면 -1 리턴
        return -1