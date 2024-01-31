class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 모든 수를 합해도 target보다 작은 경우 0 반환
        if sum(nums) < target:
            return 0

        # target인 값이 있는 경우 1 반환
        if target in nums:
            return 1

        # 숫자 개수
        N = len(nums)

        # 합이 target 이상인 구간의 최소 길이
        min_len = N

        # 구간의 시작, 끝, 합
        left = right = 0
        s = nums[0]

        # 구간을 넓혀가면서 탐색하기
        while right < N:
            # 구간의 합이 target 이상인 경우, 길이 비교 및 왼쪽 이동
            if s >= target:
                min_len = min(min_len, right - left + 1)

                # target과 같은 경우에는 오른쪽도 이동
                if s == target:
                    right += 1
                    if right < N:
                        s += nums[right]

                s -= nums[left]
                left += 1

            # 구간의 합이 target보다 작은 경우, 구간 이동
            else:
                right += 1
                if right < N:
                    s += nums[right]

        return min_len