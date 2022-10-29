# https://school.programmers.co.kr/learn/courses/30/lessons/60061

# 구조물이 규칙을 만족하는지 확인
def check(result):
    # 구조물 하나씩 확인하기
    for x, y, a in result:
        # 기둥
        if a == 0:
            # 바닥이나 기둥이나 보 위에 있으면 OK
            if y == 0 or [x, y - 1, 0] in result or [x - 1, y, 1] in result or [x, y, 1] in result:
                continue
            else:
                return False
        # 보
        if a == 1:
            # 한 쪽이라도 기둥 위에 있으면 OK
            if [x, y - 1, 0] in result or [x + 1, y - 1, 0] in result:
                continue
            # 양쪽 모두 보에 연결되어 있으면 OK
            elif [x - 1, y, 1] in result and [x + 1, y, 1] in result:
                continue
            else:
                return False

    return True


# n: 벽면의 크기
# build_frame: 모든 작업에 대한 정보
def solution(n, build_frame):
    # 수행한 작업들의 결과물
    result = []

    # 작업 하나씩 수행하기
    for x, y, a, b in build_frame:
        # 삭제
        if b == 0:
            # 현재 작업 삭제하기
            result.remove([x, y, a])
            # 삭제했을 때의 구조물이 규칙을 만족하지 않는다면 원래대로 복구하기
            if not check(result):
                result.append([x, y, a])

        # 추가
        elif b == 1:
            # 현재 작업 추가하기
            result.append([x, y, a])
            # 추가했을 때의 구조물이 규칙을 만족하지 않는다면 원래대로 복구하기
            if not check(result):
                result.remove([x, y, a])

    result.sort()
    return result
