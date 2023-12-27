class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # nums 크기
        N = len(nums)

        # 현재까지의 점수와 현재 위치를 담은 최대 힙 (최대 힙이므로 부호를 반대로 저장)
        h = []
        heapq.heappush(h, (-nums[0], 0))

        # 현재까지의 점수가 높은 순으로 확인하며, 현재 위치에 도달할 수 없는 곳인 경우 힙에서 삭제
        # 최대 힙에 있는 모든 원소를 꺼내어서 비교하는 경우, 이중 for문을 사용하여 탐색하는 것과 같음 -> 시간 초과
        for i in range(1, N):
            # 현재 위치와 거리가 k보다 큰 곳은 꺼내기
            while h and h[0][1] < i - k:
                heapq.heappop(h)

            # 현재 위치에서의 최대 점수를 힙에 넣기 (최대 힙이므로 부호를 반대로 저장)
            heapq.heappush(h, (h[0][0] - nums[i], i))
                
        # 마지막 위치가 나올 때까지 꺼내기
        while h[0][1] != N - 1:
            heapq.heappop(h)

        return -h[0][0]