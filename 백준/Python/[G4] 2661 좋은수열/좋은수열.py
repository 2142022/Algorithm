import sys
input = sys.stdin.readline

# idx번째 숫자로 가능한 수 구하기
def find_num(idx):
    # 불가능 체크
    impossible = [0] * 4
    # 이전 숫자는 불가능
    impossible[num[idx - 1]] = 1
    # 불가능한 수 개수
    cnt = 1

    # 비교할 최대 자릿수
    digit = (idx + 1) // 2

    # 비교 자릿수 하나씩 늘려가면서 비교
    for i in range(2, digit + 1):
        # 앞의 숫자들이 모두 같으면 1, 다르면 0
        same = 1

        # 비교하는 두 수의 시작인덱스
        idx1 = idx - i + 1
        idx2 = idx1 - i

        # 하나씩 비교
        while idx1 < idx:
            if num[idx1] != num[idx2]:
                same = 0
                break
            idx1 += 1
            idx2 += 1

        # 앞의 숫자들이 모두 같은 경우
        if same:
            impossible[num[idx2]] = 1
            cnt += 1

            # 모든 숫자가 불가능하면 끝내기
            if cnt == 3:
                return []

    # 가능한 숫자 반환
    return [i for i in range(1, 4) if impossible[i] == 0]

#################################################################

# DFS로 수열 구하기
# idx: 현재 채워야 하는 숫자의 인덱스
def dfs(idx):
    global N

    # 다 채운 경우 끝내기
    if idx == N:
        print(int(''.join(map(str, num))))
        exit()

    # 다음 숫자로 가능한 수 구하기
    possible = find_num(idx)

    # 다음 숫자 채우기
    for i in possible:
        num[idx] = i
        dfs(idx + 1)

#################################################################

# 수열의 길이
N = int(input())

# 수열
num = [0] * N

# DFS로 수열 구하기
for i in range(1, 4):
    num[0] = i
    dfs(1)
