class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # DFS로 target이 나올 수 있는 경우의 수 구하기
        # idx: 현재 nums의 인덱스
        # s: 현재까지의 합
        def dfs(idx, s):
            k = (idx, s)

            # 처음으로 k가 나온 경우
            if k not in cnt:
                # 탐색이 끝난 경우
                if idx == len(nums):
                    # 총합으로 target이 나왔다면 1 반환
                    if s == target:
                        return 1
                    else:
                        return 0

                # 현재 숫자를 더하거나 뺐을 때 최종적으로 target이 나오는 경우의 수
                else:
                    num = nums[idx]
                    cnt[k] = dfs(idx + 1, s + num) + dfs(idx + 1, s - num)

            return cnt[k]

        #################################################################################
        
        # (인덱스, 합)에 대한 횟수
        cnt = defaultdict(int)

        return dfs(0, 0)