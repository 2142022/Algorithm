import sys
input = sys.stdin.readline

# 테스트 케이스
for _ in range(int(input())):
    # 학생 수
    n = int(input())

    # 각 학생이 선택한 학생
    selected = [0] + list(map(int, input().split()))

    # 팀에 속할 수 있는지 체크 (1: 가능, -1: 불가능)
    join = [0] * (n + 1)

    # 팀에 속하지 못한 학생 수
    cnt = 0

    # 한 명씩 탐색
    for i in range(1, n + 1):
        # 이미 팀에 속해있거나 속해있지 않은 경우 패스
        if join[i]:
            continue

        # 선택한 학생
        s = selected[i]

        # 본인인 경우 패스
        if s == i:
            join[i] = 1
            continue

        # 탐색한 학생을 담은 스택
        stack = [i]
        # 조회를 빠르게 하기 위해 스택과 동일한 집합
        stack_set = {i}
        while stack:
            # 마지막 학생이 선택한 학생
            s = selected[stack[-1]]

            # 이미 팀에 속해 있거나 팀을 구성하지 못하는 학생인 경우,
            # 현재까지의 학생들 팀 구성 불가
            if join[s]:
                break

            # 현재 스택에 있는 학생인 경우, 그 학생까지 팀 구성 가능
            if s in stack_set:
                while stack and stack[-1] != s:
                    join[stack.pop()] = 1
                join[stack.pop()] = 1
                break

            # 현재 학생 스택에 넣기
            stack.append(s)
            stack_set.add(s)

        # 스택에 남아있는 학생들은 팀 구성 불가
        while stack:
            join[stack.pop()] = -1
            cnt += 1

    print(cnt)
