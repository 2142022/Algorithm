import sys
input = sys.stdin.readline

# string: 회문인지 확인할 문자열
# flag: 한 문자를 삭제한 문자열이라면 1, 아니면 0
def check(string, flag):
    # 앞 글자와 뒷 글자를 하나씩 비교
    for i in range(len(string) // 2):
        # 글자가 같지 않다면
        if string[i] != string[-1 - i]:
            # 이미 문자를 삭제했었다면 일반 문자열
            if flag == 1:
                return 2
            # 아직 문자열을 삭제하지 않았다면:
            else:
                # 앞 글자를 하나 삭제한 경우와 뒷 글자를 삭제한 경우 비교하기
                # 어차피 유사 회문 아니면 일반 문자열이므로 1 또는 2
                return min(check(string[i + 1 : len(string) - i], 1), check(string[i : -1 - i], 1))

    # 한 문자를 삭제했다면 유사회문
    if flag == 1:
        return 1
    # 한 문자도 삭제하지 않았다면 회문
    else:
        return 0



# 문자열의 개수
T = int(input())

for t in range(T):
    # 문자열
    string = input().rstrip()

    # 회문 체크
    print(check(string, 0))
