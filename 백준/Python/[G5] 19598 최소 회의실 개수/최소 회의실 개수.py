import sys
input = sys.stdin.readline

# 회의 개수
N = int(input())

# 회의 정보
# 시작 시간은 1, 끝나는 시간은 -1과 함께 저장
meeting = []
for _ in range(N):
    # s: 회의 시작 시간, f: 회의 끝나는 시간
    s, f = map(int, input().split())

    meeting.append((s, 1))
    meeting.append((f, -1))

# 오름차순 정렬
meeting.sort()

# 필요한 회의실의 최소 개수
cnt = 0

# 시작 시간이면 1, 끝나는 시간이면 -1 더하기
tmp = 0
for i in range(2 * N):
    tmp += meeting[i][1]
    cnt = max(cnt, tmp)

print(cnt)