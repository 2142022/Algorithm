import sys
input = sys.stdin.readline

# 파일의 패턴 일치 여부 확인하는 함수
def check(file):
    # 패턴에서 별표를 뺀 길이가 파일 이름보다 길다면 겹치게 되므로 항상 false
    if len(pattern) - 1 > len(file):
        return False

    # 별표가 나올 때까지 앞에서부터 검사
    i = 0
    while pattern[i] != '*':
        if i < len(file) and file[i] != pattern[i]:
            return False
        i += 1

    # 별표가 나올 때까지 뒤에서부터 검사
    j = -1
    while pattern[j] != '*':
        if abs(j) <= len(file) and file[j] != pattern[j]:
            return False
        j -= 1

    return True

#########################################

# 파일의 개수
N = int(input())

# 패턴
pattern = list(input())

# N개의 파일 검사
for _ in range(N):
    # 검사할 파일 이름
    file = list(input())

    # 일치 여부 검사
    if check(file):
        print("DA")
    else:
        print("NE")