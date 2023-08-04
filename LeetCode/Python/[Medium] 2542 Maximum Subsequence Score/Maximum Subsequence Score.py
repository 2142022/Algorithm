# https://leetcode.com/problems/maximum-subsequence-score/submissions/?envType=study-plan-v2&envId=leetcode-75

import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # num1에서 k개의 합
        s = 0
        # 최대 점수
        score = 0
        
        # num1과 num2의 원소를 순서대로 묶은 리스트
        nums = list(zip(nums1, nums2))
        
        # nums2의 원소를 기준으로 내림차순 정렬
        nums.sort(key = lambda x : x[1], reverse = True)

        # nums1에서 뽑은 원소들의 최소 힙
        h = []

        # 원소 뽑기
        for a, b in nums:
            # 합 더하고 최소 힙 추가
            s += a
            heapq.heappush(h, a)

            # 힙에 k개보다 많은 경우 하나 빼기
            if len(h) > k:
                s -= heapq.heappop(h)
            
            # 힙의 원소가 k개가 되는 경우 최대 점수 비교
            if len(h) == k:
                score = max(score, s * b)

        return score