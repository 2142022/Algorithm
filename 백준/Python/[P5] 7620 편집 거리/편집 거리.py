import sys
input = sys.stdin.readline

# A를 B로 바꾸기 위해 필요한 최소 편집 스크립트 구하기
def edit(a, b):
    # A, B의 크기
    n, m = len(a), len(b)

    # dp와 인덱스를 맞추기 위해 공백 추가
    a, b = ' ' + a, ' ' + b

    # 문자열 a의 크기가 1인 경우
    if n == 1:
        # a를 b로 바꾸는데 필요한 최소 편집 거리
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(m + 1):
            dp[0][i] = i
        dp[1][0] = 1

        for i in range(1, m + 1):
            # 같은 문자인 경우, 왼쪽 상단에서 가져오기
            if a[1] == b[i]:
                dp[1][i] = dp[0][i - 1]
            # 다른 문자인 경우, 추가(좌), 삭제(상), 수정(좌상) 중 최소 편집 거리 + 1
            else:
                dp[1][i] = min(dp[1][i - 1], min(dp[0][i - 1], dp[0][i])) + 1

        # 편집 스크립트
        script = []
        while n != 0 or m != 0:
            # 추가
            if n == 0 and m != 0:
                script.append(('a', b[m]))
                m -= 1
                continue
            # 삭제
            elif n != 0 and m == 0:
                script.append(('d', a[n]))
                n -= 1
                continue

            # 좌, 상, 좌상 중 최소값
            mn = min(dp[n - 1][m], min(dp[n - 1][m - 1], dp[n][m - 1]))

            # 수정 or 복사
            if dp[n - 1][m - 1] == mn:
                if dp[n][m] == mn:
                    script.append(('c', a[n]))
                else:
                    script.append(('m', b[m]))
                n -= 1
                m -= 1

            # 삭제
            elif dp[n - 1][m] == mn:
                script.append(('d', ' '))
                n -= 1

            # 추가
            else:
                script.append(('a', b[m]))
                m -= 1

        # 반대로 출력
        for i in script[::-1]:
            print(*i)
        return

    # 탐색 구간 나누기
    prev = [i for i in range(m + 2)]
    up = [0] * (m + 2)
    down = [0] * (m + 2)
    middle = n // 2

    # 윗 부분
    for i in range(1, middle + 1):
        up[0] = i
        for j in range(1, m + 1):
            if a[i] == b[j]:
                up[j] = prev[j - 1]
            else:
                up[j] = min(up[j - 1], min(prev[j], prev[j - 1])) + 1
        prev = up[:]

    # 아래 부분
    for i in range(m + 1, 0, -1):
        prev[i] = m + 1 - i
    for i in range(n, middle, -1):
        down[m + 1] = n - i + 1
        for j in range(m, 0, -1):
            if a[i] == b[j]:
                down[j] = prev[j + 1]
            else:
                down[j] = min(down[j + 1], min(prev[j], prev[j + 1])) + 1
        prev = down[:]

    # 최소 값을 가지는 열 정하기
    mn = sys.maxsize
    idx = 0
    for i in range(len(up) - 1):
        if mn > up[i] + down[i + 1]:
            mn = up[i] + down[i + 1]
            idx = i

    # 재귀로 분할된 구간 탐색
    edit(a[1:middle + 1], b[1:idx + 1])
    edit(a[middle + 1:], b[idx + 1:])

######################################################################################

# 원래 문자열
A = input().rstrip()
# 바꿀 문자열
B = input().rstrip()

# 가장 짧은 편집 스크립트 구하기
edit(A, B)

