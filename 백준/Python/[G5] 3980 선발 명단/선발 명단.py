import sys
input = sys.stdin.readline

# idx번째 선수의 포지션 배치 (ability: 현재까지 배치된 선수들의 능력치 합)
def lineup(idx, ability):
    global max_ability
    
    # 모든 선수가 배치되어 있으면 끝내기
    if idx == 11:
        max_ability = max(max_ability, ability)
        return
    
    for i in range(11):
        # 능력치가 0이거나 이미 누군가 배치되어 있으면 배치 불가능
        if S[idx][i] == 0 or flag[i] == 1:
            continue

        # 현재 포지션에 배치
        flag[i] = 1

        # 재귀로 다음 선수의 포지션 구하기
        lineup(idx + 1, ability + S[idx][i])

        # 다른 경우를 위해 현재 포지션 배치 취소
        flag[i] = 0

   

# 테스트케이스 개수
C = int(input())

# C개의 테스트케이스
for c in range(C):
    # 각 선수들의 능력
    S = [list(map(int, input().split())) for i in range(11)]

    # 능력치 합 최대값
    max_ability = 0

    # i번째 포지션이 이미 배치되어 있으면 flag[i] = 1
    flag = [0] * 11

    # 라인업 구하기
    lineup(0, 0)

    print(max_ability)
