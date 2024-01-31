import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

# 제거되는 사람 인덱스 구하기
def f(n, k):
    # 남은 사람이 한 명일 경우, 0
    if n == 1:
        return 0

    # 제거 간격이 1이라면 마지막 사람 반환
    if k == 1:
        return n - 1

    if k < n:
        # ex) 7명(n)에서 3번째(k) 사람을 제거한다면 한 번에 2명(d) 제거 가능함
        #     마지막 남은 1명(m)만큼 빼줘야 인덱스가 앞으로 당겨짐
        # (f(n - d, k) - m) % (n - d): 마지막으로 삭제된 사람의 이전 인원에서의 인덱스
        # k * ((f(n - d, k) - m) % (n - d)) // (k - 1) : 마지막으로 삭제된 사람의 현재 인원에서의 인덱스
        d, m = divmod(n, k)
        return k * ((f(n - d, k) - m) % (n - d)) // (k - 1)

    return (f(n - 1, k) + k) % n

# 사람 수, 제거하는 사람 번호
N, K = map(int, input().split())

# 점화식: f(N, K) = (f(N - 1, K) + K) mod N
# 사람의 번호가 1부터 시작하므로 +1
print(f(N, K) + 1)