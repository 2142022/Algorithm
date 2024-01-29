# 10개의 테스트케이스
for t in range(1, 11):
    # 문자열 길이, 문자열
    N, s = input().split()
    N = int(N)

    # 비밀번호
    password = []
    for c in s:
        # 이전과 같은 문자라면 소거
        if password and password[-1] == c:
            password.pop()
        # 다른 문자라면 저장
        else:
            password.append(c)

    print(f'#{t} {"".join(password)}')
