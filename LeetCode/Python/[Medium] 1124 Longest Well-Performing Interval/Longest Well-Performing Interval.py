class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # 일한 날 수
        N = len(hours)

        # 가장 긴 well-performing 간격
        interval = 0

        # 피곤한 날은 1, 안 피곤한 날은 -1로 계산했을 때의 누적합
        s = 0
        
        # 누적합 값을 처음 가지게 되는 인덱스
        idx = defaultdict(int)

        # 누적합 구하기
        for i in range(N):
            # 피곤한 날은 1, 안 피곤한 날은 -1
            s += 1 if hours[i] > 8 else -1

            # 현재까지의 모든 날들이 well-performing인 경우
            if s > 0:
                interval = i + 1
            # 그 외에는 (현재 누적합 값 - 1)을 처음 가지게 되는 인덱스와의 차이 생각하기
            # (현재 누적합 - (현재 누적합 - 1))은 1이므로 well-performing이기 때문
            elif s - 1 in idx:
                interval = max(interval, i - idx[s - 1])

            # 현재 누적합 값이 처음 나오는 경우 인덱스 저장
            if s not in idx:
                idx[s] = i

        return interval
