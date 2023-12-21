class Solution:
    def numTilings(self, n: int) -> int:
        # 나눌 수 
        m = 10 ** 9 + 7

        # 가로의 길이가 i일때 만들 수 있는 경우의 수
        cnt = [1] * (n + 1)

        # 점화식(n >= 4): cnt[n] = (cnt[n-1] + cnt[n-2]) + 2*(cnt[n-3] + ... + cnt[1]) + 2
        # n=2일 때 2, n=3일 때 5
        # s: cnt[1] + ... cnt[n-3]
        s = 0
        for i in range(2, n + 1):
            if i == 2:
                cnt[i] = 2
            elif i == 3:
                cnt[i] = 5
            else:
                s = (s + cnt[i - 3]) % m
                cnt[i] = (cnt[i - 1] + cnt[i - 2] + 2 * s + 2) % m

        return cnt[n]