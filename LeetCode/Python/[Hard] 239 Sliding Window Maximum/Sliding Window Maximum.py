class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 탐색하는 구간의 최대값
        result = []

        # 구간별 최대값의 인덱스를 담은 큐
        q = deque()
        for i in range(len(nums)):
            # 탐색하는 구간이 아닌 인덱스 삭제
            if q and q[0] <= i - k:
                q.popleft()

            # 현재 값보다 작은 값인 경우, 큐에서 인덱스 삭제
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            # 현재 인덱스 추가
            q.append(i)

            # 큐의 첫 번째 원소는 현재 구간의 최대값의 인덱스가 담겨 있는 상태
            result.append(nums[q[0]])

        return result[k - 1:]