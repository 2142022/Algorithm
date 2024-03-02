class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # 원소가 2개 미만인 경우
        N = len(nums)
        if N < 2:
            return False

        # 누적합을 k로 나눴을 때의 나머지가 나온 첫 인덱스
        idx = defaultdict(int)
        
        # 마지막 누적합의 나머지
        num = nums[0] % k
        idx[num] = 0

        # 누적합
        for i in range(1, N):
            num = (num + nums[i]) % k

            # 나머지가 0인 경우, k 배수
            if num == 0:
                return True

            # 이전에 같은 나머지를 가진 누적합이 있는 경우 뺐을 때 k의 배수가 됨
            # 단, 원소의 개수가 2개 이상이어야 함
            if num in idx and i - idx[num] >= 2:
                return True

            # 처음 나온 나머지라면 현재 인덱스 저장
            elif num not in idx:
                idx[num] = i

        # 탐색이 끝났지만 k의 배수를 가진 subarray가 없는 경우
        return False