from collections import defaultdict
import sys
input = sys.stdin.readline

# 빙고판에 있는 숫자의 위치
pos = defaultdict(list)
for i in range(5):
    info = list(map(int, input().split()))
    for j in range(5):
        pos[info[j]] = [i, j]

# 사회자가 부른 숫자
nums = []
for _ in range(5):
    nums += list(map(int, input().split()))

# 행별 체크한 개수
row = [0] * 5
# 열별 체크한 개수
col = [0] * 5
# 대각선별 체크한 개수
dg = [0] * 2

# 선 긋는 횟수
cnt = 0
for k in range(25):
    num = nums[k]

    # 사회자가 부른 숫자 체크 후, 5개가 다 채워진 경우 선 개수 추가
    i, j = pos[num]
    # 가로
    row[i] += 1
    if row[i] == 5:
        cnt += 1
    # 세로
    col[j] += 1
    if col[j] == 5:
        cnt += 1
    # 대각선 (오른쪽 하단)
    if i == j:
        dg[0] += 1
        if dg[0] == 5:
            cnt += 1
    # 대각선 (왼쪽 상단)
    if i + j == 4:
        dg[1] += 1
        if dg[1] == 5:
            cnt += 1

    # 빙고를 외칠 수 있는 경우 끝내기
    if cnt >= 3:
        print(k + 1)
        break
