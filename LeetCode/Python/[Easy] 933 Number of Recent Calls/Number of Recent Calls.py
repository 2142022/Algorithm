class RecentCounter:

    def __init__(self):
        # 요청한 시간
        self.time = deque()

    def ping(self, t: int) -> int:
        # 현재 시간 추가
        self.time.append(t)

        # t - 3000 전 요청 삭제
        while self.time and self.time[0] < t - 3000:
            self.time.popleft()
            
        # 최근 요청 수 반환
        return len(self.time)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)