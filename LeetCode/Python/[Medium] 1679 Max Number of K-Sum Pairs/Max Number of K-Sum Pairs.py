class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # 오름차순 정렬
        nums.sort()

        # 왼쪽 인덱스
        idx1 = 0
        # 오른쪽 인덱스
        idx2 = len(nums) - 1

        # 최대 연산 횟수
        cnt = 0

        # 모든 수를 다 탐색할 때까지 반복
        while idx1 < idx2:
            # 현재 두 수의 합
            s = nums[idx1] + nums[idx2]

            # 두 수의 합이 k라면 연산 횟수 증가
            if s == k:
                cnt += 1
                idx1 += 1
                idx2 -= 1

            # 두 수의 합이 k보다 크다면 오른쪽 인덱스 감소
            elif s > k:
                idx2 -= 1
            
            # 두 수의 합이 k보다 작다면 왼쪽 인덱스 증가
            else:
                idx1 += 1

        return cnt