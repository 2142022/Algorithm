import sys
input = sys.stdin.readline

# 알파벳 별 위치 (왼손, 오른손 나눠서)
left = {'q': (0, 0), 'w': (0, 1), 'e': (0, 2), 'r': (0, 3), 't': (0, 4), 'a': (1, 0), 's': (1, 1), 'd': (1, 2), 'f': (1, 3), 'g': (1, 4), 'z': (2, 0), 'x': (2, 1), 'c': (2, 2), 'v': (2, 3)}
right = {'y': (0, 1), 'u': (0, 2), 'i': (0, 3), 'o': (0, 4), 'p': (0, 5), 'h': (1, 1), 'j': (1, 2), 'k': (1, 3), 'l': (1, 4), 'b': (2, 0), 'n': (2, 1), 'm': (2, 2)}

# 손가락 위치
SL, SR = input().split()
lr, lc = left[SL]
rr, rc = right[SR]

# 최소 시간
time = 0

# 출력할 문자열
s = input().rstrip()
for alpha in s:
    # 자음
    if alpha in left:
        # 출력할 문자의 위치
        pr, pc = left[alpha]

        # 시간 증가 및 위치 변경
        time += abs(lr - pr) + abs(lc - pc)
        lr, lc = pr, pc

    # 모음
    else:
        # 출력할 문자의 위치
        pr, pc = right[alpha]

        # 시간 증가 및 위치 변경
        time += abs(rr - pr) + abs(rc - pc)
        rr, rc = pr, pc

# 문자 입력하는 시간만큼 증가
print(time + len(s))