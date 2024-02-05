class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # 인원
        N = len(senate)

        # Radient / Dire의 권리를 가진 사람의 인덱스
        r = deque()
        d = deque()
        for i, c in enumerate(senate):
            if c == 'R':
                r.append(i)
            else:
                d.append(i)

        # 게임 진행
        while True:
            # 한 팀의 인원이 없는 경우 끝내기
            if not r:
                return 'Dire'
            if not d:
                return 'Radiant'

            # 현재 턴이 'Radiant'팀인 경우
            if r[0] < d[0]:
                r.append(r.popleft() + N)
                d.popleft()

            # 현재 턴이 'Dire'팀인 경우
            else:
                d.append(d.popleft() + N)
                r.popleft()