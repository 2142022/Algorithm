import sys
input = sys.stdin.readline

# 축약된 IPv6
shorten = input().rstrip()

# 콜론 개수
colon = shorten.count(':')

# 0으로만 이루어진 그룹이 있는 경우 필요한 만큼 콜론 추가
if colon < 7:
    idx = shorten.index('::')
    shorten_list = list(shorten)
    for _ in range(7 - colon):
        shorten_list.insert(idx, ':')
    shorten = ''.join(shorten_list)
# 0으로만 이루어진 그룹 하나가 양 끝에 있는 경우 콜론 하나 삭제
elif colon == 8:
    idx = shorten.index("::")
    shorten_list = list(shorten)
    shorten_list.pop(idx)
    shorten = ''.join(shorten_list)

# 콜론 단위로 분리하기
ip = list(shorten.split(':'))
for i in range(8):
    # 해당 그룹에서 부족한 만큼 0 채우기
    ip[i] = '0' * (4 - len(ip[i])) + ip[i]

# 문자열로 나타내기
print(':'.join(ip))