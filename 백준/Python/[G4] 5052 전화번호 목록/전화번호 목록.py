import sys
input = sys.stdin.readline

# 전화번호의 일관성 체크
def check(phone):
    # p1: 접두어인지 확인할 전화번호
    # p2: p1이 접두어에 있는지 확인할 전화번호
    for p1, p2 in zip(phone, phone[1:]):
        if p2.startswith(p1):
            return False
    return True

######################################################

# 테스트케이스 개수
t = int(input())
for _ in range(t):
    # 전화번호 개수
    n = int(input())

    # 전화번호 목록
    phone = [input().strip() for _ in range(n)]

    # 일관성 체크
    # 순서대로 한번씩만 체크하기 위해 정렬하기
    if check(sorted(phone)):
        print('YES')
    else:
        print('NO')