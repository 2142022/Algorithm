class Solution:
    def numTilings(self, n: int) -> int:
        # 나눌 수
        m = 10 ** 9 + 7

        # 가로의 길이가 i일때 만들 수 있는 경우의 수
        cnt = [1] * (n + 1)

        # n = 1일 때 1, n = 2일 때 2
        # 점화식(n >= 3): cnt[n] = (cnt[n-1] + cnt[n-2]) + 2 X (cnt[n-3] + ... + cnt[1] + cnt[0])
        # 양 끝이 tromino로 만들 수 있는 경우가 2개씩 있음
        # 양 끝은 tromino로 그 사이는 1X2 domino로 채우기 (그렇지 않으면 딱 나눠떨어지기 때문에 이전 cnt에 포함되어 있음)
        # ex) n = 6일 때
        #   앞에는 cnt[5] & 5번째 열부터 {| 1개}                                                                            => cnt[5]
        #   앞에는 cnt[4] & 4번째 열부터 {위 ㅡ 1개, 아래 1개}                                                               => cnt[4]
        #   0번째 열부터 {ㄴ, 위 ㅡ 2개, 아래 ㅡ 1개, ㄴ 좌우반전}, {ㄱ 좌우반전, 위 ㅡ 1개, 아래 ㅡ 2개, ㄱ}                  => 2 X cnt[0]
        #   앞에는 cnt[1] & 1번째 열부터 {ㄴ, 위 ㅡ 1개, 아래 ㅡ 1개, ㄱ}, {ㄱ 좌우반전, 위 ㅡ 1개, 아래 ㅡ 1개, ㄴ 좌우반전}  => 2 X cnt[1]
        #   앞에는 cnt[2] & 2번째 열부터 {ㄴ, 위 ㅡ 1개, ㄴ 좌우반전}, {ㄱ 좌우반전, 아래 ㅡ 1개, ㄱ}                         => 2 X cnt[2]
        #   앞에는 cnt[3] & 3번째 열부터 {ㄴ, ㄱ}, {ㄱ 좌우반전, ㄴ 좌우반전}                                                => 2 X cnt[3]

        # 위의 점화식 정리 (n >= 3)
        # cnt[n] = (cnt[n-1] + cnt[n-2]) + 2 X (cnt[n-3] + ... + cnt[1] + cnt[0])
        #        = cnt[n-1] + cnt[n-3] + {cnt[n-2] + cnt[n-3] + 2 X (cnt[n-4] + ... + cnt[1] + cnt[0])}
        #        = cnt[n-1] + cnt[n-3] + cnt[n-1]
        #        = 2 X cnt[n-1] + cnt[n-3]
        
        for i in range(2, n + 1):
            if i == 2:
                cnt[i] = 2
            else:
                cnt[i] = (2 * cnt[i - 1] + cnt[i - 3]) % m

        return cnt[n]