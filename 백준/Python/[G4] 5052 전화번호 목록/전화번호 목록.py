import sys
input = sys.stdin.readline

# 전화번호가 일관성이 있는지 확인
def consistency():
    # 전화번호가 1개면 항상 일관성 있음
    if n == 1:
        return True

    # 탐색 전화번호가 다음 전화번호의 접두어인지 확인
    for i in range(n - 1):
        if nums[i + 1].startswith(nums[i]):
            return False
    return True

############################################################

# 테스트 케이스
for _ in range(int(input())):
    # 전화번호 수
    n = int(input())

    # 모든 전화번호 (사전순 정렬)
    nums = sorted([input().rstrip() for _ in range(n)])

    # 전화번호가 일관성이 있는지 확인
    if consistency():
        print('YES')
    else:
        print('NO')