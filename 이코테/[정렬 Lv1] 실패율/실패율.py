# https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    # 사용자 수
    L = len(stages)

    # 전 스테이지에서 실패한 사용자 수
    cnt = 0

    # 각 스테이지별 실패율을 담은 리스트
    fail = []
    j = 0
    for i in range(1, N + 1):
        # 현재 스테이지에 도달한 사람이 없는 경우
        if L - cnt == 0:
            fail.append((0, i))
            continue

        # 현재 스테이지에서 실패한 사용자 수
        now = 0
        for j in stages:
            if j == i:
                now += 1

        # 현재 스테이지의 실패율 구하기
        # 현재 스테이지에 도달했지만 실패한 사람의 수: now
        # 현재 스테이지에 도달한 사람의 수: L - cnt
        fail.append((now / (L - cnt), i))

        cnt += now

    # 실패율 기준 내림차순 정렬
    fail.sort(key = lambda x : (-x[0], x[1]))

    # 실패율 기준 내림차순 정렬된 스테이지 번호
    answer = [0] * N
    for i in range(N):
        answer[i] = fail[i][1]

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))