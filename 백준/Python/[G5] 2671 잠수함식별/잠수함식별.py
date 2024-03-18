import sys
input = sys.stdin.readline

# 잠수함 엔진 소리인지 아닌지 판별
def judge():
    for sound in sounds:
        # 4개 미만 크기이거나, 처음이나 마지막이 0으로 끝나면 잡음
        if len(sound) < 4 or sound[0] == 0 or sound[-1] == 0:
            return "NOISE"

        # 맨 앞과 뒤를 제외하고 1의 개수가 1개인 경우 잡음
        start, end = 0, len(sound) - 1
        while start < len(sound) and sound[start]:
            start += 1
        while end >= 0 and sound[end]:
            end -= 1
        while start < end:
            # 0인 경우 패스
            if sound[start] == 0:
                start += 1
                continue

            # 연속된 1의 개수 세기
            cnt = 1
            while start + cnt < end and sound[start + cnt]:
                cnt += 1

            # 1이 1개인 경우 잡음
            if cnt == 1:
                return "NOISE"
            else:
                start += cnt

    return "SUBMARINE"

##########################################################################

# 소리
S = list(map(int, input().rstrip()))

# 2개 미만 크기이거나 마지막이 0으로 끝나면 잡음
if len(S) < 2 or S[-1] == 0:
    print("NOISE")

else:
    # '01'을 기준으로 소리 나누기
    sounds = []
    pos = [-2]
    i = 0
    while i < len(S):
        # 0이 아닌 경우 패스
        if S[i]:
            i += 1
            continue

        # 0의 개수 세기
        cnt = 1
        while i + cnt < len(S) and S[i + cnt] == 0:
            cnt += 1

        # 0이 1개인 경우, 01
        if cnt == 1:
            pos.append(i)
            i += 2

        # 0이 여러개인 경우 패스
        else:
            i += cnt + 1

    # '01'을 기준으로 소리 나누기
    pos.append(len(S))
    for i in range(len(pos) - 1):
        s = S[pos[i] + 2:pos[i + 1]]
        if s:
            sounds.append(s)

    # 각 소리가 엔진소리인지 잡음인지 확인
    print(judge())