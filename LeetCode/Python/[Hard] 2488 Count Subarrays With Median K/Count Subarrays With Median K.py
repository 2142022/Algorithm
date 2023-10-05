class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # k의 인덱스
        idx = nums.index(k)

        # k를 기점으로 왼쪽으로 탐색했을 때, k보다 작으면 -1, k보다 크면 1
        # 그리고 그 값들을 순차적으로 더했을 때의 값의 개수
        # [k]를 고려하여 sum_cnt[0] = 1
        sum_cnt = defaultdict(int)
        sum_cnt[0] = 1

        # k를 기점으로 왼쪽으로 탐색할 때의 누적합
        s = 0
        for i in range(idx - 1, -1, -1):
            # 현재 값
            n = nums[i]

            # 현재 값이 k보다 작으면 -1, k보다 크면 1 더하기
            if n > k:
                s += 1
            else:
                s -= 1

            # 현재까지의 누적합의 개수 갱신
            sum_cnt[s] += 1

        # k가 중앙값인 경우는 누적합이 0이거나 1인 경우
        cnt = sum_cnt[0] + sum_cnt[1]

        # k를 기점으로 오른쪽으로 탐색할 때의 누적합
        s = 0
        for i in range(idx + 1, len(nums)):
            # 현재 값
            n = nums[i]

            # 현재 값이 k보다 작으면 -1, k보다 크면 +1 더하기
            if n > k:
                s += 1
            else:
                s -= 1

            # 현재 누적합이 -3이라면, 왼쪽으로 탐색했을 때 +3이나 +4가 되어야 총 누적합이 0이나 1이 됨
            # k가 중앙값인 경우의 수 갱신
            cnt += sum_cnt[-s] + sum_cnt[-s + 1]

        return cnt
