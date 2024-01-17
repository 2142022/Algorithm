class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 숫자 개수
        N = len(nums)
        
        # 투포인터 사용하기 위해 정렬
        nums.sort()
        
        # 중복 제거를 위해 set으로 설정
        triplets = set()
    
        # 첫 번째 숫자의 인덱스
        for i in range(N):
            
            # 두번째, 세번째 숫자의 인덱스
            j, k = i + 1, N - 1
            
            # 두번째 숫자가 더 작을 때까지 탐색
            while j < k:
                # 세 숫자
                a, b, c = nums[i], nums[j], nums[k]
                
                # 세 숫자의 합
                s = a + b + c
                
                # 합이 0이 되면 결과 추가
                if s == 0:
                    triplets.add((a, b, c))
                    j += 1
                    k -= 1
                    
                # 합이 음수라면 두 번째 숫자 높이기
                elif s < 0:
                    j += 1
                    
                # 합이 양수라면 세 번째 숫자 낮추기
                elif s > 0:
                    k -= 1
                
        # 리스트로 변환
        return list(triplets)