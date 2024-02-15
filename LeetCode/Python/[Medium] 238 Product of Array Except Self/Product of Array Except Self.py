class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 숫자 개수
        N = len(nums)

        # 자신을 제외한 수들의 곱
        product = [1] * N

        # 앞에서부터 하나씩 곱해서 다음 위치에 저장
        prefix = 1
        for i in range(N):
            product[i] = prefix
            prefix *= nums[i]

        # 뒤에서부터 하나씩 곱해서 다음 위치에 저장
        suffix = 1
        for i in range(N - 1, -1, -1):
            product[i] *= suffix
            suffix *= nums[i]

        return product