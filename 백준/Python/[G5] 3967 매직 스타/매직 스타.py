import sys
input = sys.stdin.readline

# 재귀로 한 칸씩 채우기
def dfs(i):
    # 모두 채운 경우 끝내기
    if i == 12:
        A = [[0] * 9 for _ in range(5)]
        A[0][4], A[1][1], A[1][3], A[1][5], A[1][7], A[2][2], A[2][6], A[3][1], A[3][3], A[3][5], A[3][7], A[4][4] = nums
        for a in A:
            print(''.join(list(map(lambda x: chr(x + 64) if x > 0 else '.', a))))
        exit()

    # 1, 2, 3, 4, 6, 7, 10번째 숫자
    if i in (0, 1, 2, 3, 5, 6, 9):
        # 이미 정해져 있는 경우
        if nums[i] > 0:
            dfs(i + 1)
        # 숫자 정하기
        else:
            for j in range(1, 13):
                if not used[j]:
                    used[j], nums[i] = 1, j
                    dfs(i + 1)
                    used[j] = nums[i] = 0

    # 5번째 숫자
    elif i == 4:
        # 이미 정해져 있는 경우
        if nums[i] > 0:
            if sum(nums[i - 3:i + 1]) == 26:
                dfs(i + 1)
            else:
                return
        # 숫자 정하기
        else:
            num = 26 - sum(nums[i - 3:i])
            if num <= 12 and not used[num]:
                used[num], nums[i] = 1, num
                dfs(i + 1)
                used[num] = nums[i] = 0
            else:
                return

    # 8번째 숫자
    elif i == 7:
        # 이미 정해져 있는 경우
        if nums[i] > 0:
            if nums[0] + nums[2] + nums[5] + nums[i] == 26:
                dfs(i + 1)
            else:
                return
        # 숫자 정하기
        else:
            num = 26 - nums[0] - nums[2] - nums[5]
            if num <= 12 and not used[num]:
                used[num], nums[i] = 1, num
                dfs(i + 1)
                used[num] = nums[i] = 0
            else:
                return

    # 9번째 숫자
    elif i == 8:
        # 이미 정해져 있는 경우
        if nums[i] > 0:
            if nums[3] + nums[4] + nums[6] == nums[5] + nums[7] + nums[i]:
                dfs(i + 1)
            else:
                return
        # 숫자 정하기
        else:
            num = nums[3] + nums[4] + nums[6] - nums[5] - nums[7]
            if num <= 12 and not used[num]:
                used[num], nums[i] = 1, num
                dfs(i + 1)
                used[num] = nums[i] = 0
            else:
                return

    # 11번째 숫자
    elif i == 10:
        # 이미 정해져 있는 경우
        if nums[i] > 0:
            if nums[0] + nums[3] + nums[6] + nums[i] == 26 and sum(nums[i - 3:i + 1]) == 26:
                dfs(i + 1)
            else:
                return
        # 숫자 정하기
        else:
            num = 26 - sum(nums[i - 3:i])
            if num <= 12 and not used[num] and nums[0] + nums[3] + nums[6] + num == 26:
                used[num], nums[i] = 1, num
                dfs(i + 1)
                used[num] = nums[i] = 0
            else:
                return

    # 12번째 숫자
    elif i == 11:
        # 이미 정해져 있는 경우
        if nums[i] > 0:
            if nums[1] + nums[5] + nums[8] + nums[i] == 26 and nums[4] + nums[6] + nums[9] + nums[i] == 26:
                dfs(i + 1)
            else:
                return
        # 숫자 정하기
        else:
            num = 26 - nums[1] - nums[5] - nums[8]
            if num <= 12 and not used[num] and nums[4] + nums[6] + nums[9] + num == 26:
                used[num], nums[i] = 1, num
                dfs(i + 1)
                used[num] = nums[i] = 0
            else:
                return

##############################################################################################################################################

# 매직 스타 위치를 1차원으로 생각하기
nums = []
# 사용한 숫자
used = [0] * 13
used[0] = 1
for i in range(5):
    row = input().rstrip()
    for c in row:
        if c == 'x':
            nums.append(0)
        elif 'A' <= c <= 'L':
            num = ord(c) - ord('A') + 1
            nums.append(num)
            used[num] = 1

# 재귀로 한 칸씩 채우기
dfs(0)