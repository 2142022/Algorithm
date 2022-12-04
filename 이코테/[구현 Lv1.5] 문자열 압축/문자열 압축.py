# https://school.programmers.co.kr/learn/courses/30/lessons/60057?language=python3

# 문자열 s를 unit 단위로 자르기
def shorten(s, unit):
    # 압축 문자열의 길이
    l = unit

    # 기준 문자열과 동일한 문자열의 개수
    cnt = 1

    for i in range(unit, len(s) + 1, unit):
        # 남은 문자열의 길이가 unit보다 작다면 비교 하지 않고 끝내기
        if len(s) - i < unit:
            l = l + len(s) - i
            break

        # 기준 문자열과 같으면 1, 아니면 0
        flag = 1

        # 기준 문자열과 같은지 체크
        for j in range(unit):
            if s[i + j] != s[i + j - unit]:
                flag = 0
                break

        # 기준 문자열과 같은 경우
        if flag == 1:
            # 처음으로 기준 문자열과 같은 경우나 기준 문자열의 개수가 처음으로 10개, 100개, 1000개가 되는 경우 +1
            if cnt == 1 or cnt == 9 or cnt == 99 or cnt == 999:
                l += 1

            cnt += 1

        # 기존 문자열과 다른 경우
        else:
            l += unit
            cnt = 1

    return l


def solution(s):
    # 문자열의 길이
    l = len(s)

    # 압축 문자열의 최소 길이 (문자열의 길이로 초기화)
    min_len = l

    # 문자열을 2개 ~ (문자열의 길이의 반)씩 자르기
    for i in range(1, l // 2 + 1):
        min_len = min(min_len, shorten(s, i))

    return min_len
