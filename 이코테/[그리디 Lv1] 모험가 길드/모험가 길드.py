import sys
input = sys.stdin.readline

# 모험가 수
N = int(input())

# N명의 모험가들의 공포도
fear = list(map(int, input().split()))

# 공포도 순으로 오름차순 정렬
fear.sort()

# 그룹 수
cnt = 0

# 모든 모험가 탐색
n = 0
while n < N:
    # 현재 그룹의 인원 수: n번째 모험가의 공포도
    p = fear[n]

    # 현재 그룹의 인원이 남은 모험가의 수를 넘는다면 끝내기
    if n + p > N:
        break

    # 그룹을 만들 수 있으면 1, 아니면 0
    flag = 1

    # 현재 그룹의 마지막 사람 구하기
    while fear[n + p - 1] > p:
        # 그룹의 마지막 사람이 인덱스를 초과한다면 그룹을 만들 수 없음
        if n + fear[n + p - 1] > N:
            flag = 0
            break

        p = fear[n + p - 1]

    if flag == 1:
        cnt += 1
        n += p
    else:
        break

print(cnt)