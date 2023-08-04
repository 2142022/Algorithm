# https://leetcode.com/problems/total-cost-to-hire-k-workers/?envType=study-plan-v2&envId=leetcode-75

import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # 총 비용 
        total = 0

        # 양쪽으로 최소 힙을 나누기 위한 인덱스
        # 공통되는 부분이 있을 수도 있으므로 idx2 주의
        idx1 = candidates - 1
        idx2 = max(len(costs) - candidates, candidates)

        # 최소 힙 생성
        left = costs[:idx1 + 1]
        right = costs[idx2:]
        heapq.heapify(left)
        heapq.heapify(right)

        # k명 뽑기
        for _ in range(k):
            # 최소값이 left에 있는 경우 (right가 비어있는 경우 주의)
            if len(right) == 0 or (len(left) > 0 and left[0] <= right[0]):
                total += heapq.heappop(left)

                # left에 원소 1개 추가
                if idx1 + 1 < idx2:
                    heapq.heappush(left, costs[idx1 + 1])
                    idx1 += 1
                
            # 최소값이 right에 있는 경우
            else:
                total += heapq.heappop(right)

                # right에 원소 1개 추가
                if idx2 - 1 > idx1:
                    heapq. heappush(right, costs[idx2 - 1])
                    idx2 -= 1

        return total