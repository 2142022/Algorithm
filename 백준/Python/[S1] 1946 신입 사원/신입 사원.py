import sys

# 테스트케이스 개수
T = int(sys.stdin.readline())

# T개의 테스트케이스
for t in range(T):
    # 지원자 수
    N = int(sys.stdin.readline())

    # 성적 입력받기
    rank = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

    # 서류 성적 순위 기준으로 오름차순 정렬
    rank.sort()

    # 서류 1등 -> 합격자
    cnt = 1
    min = rank[0][1]

    # rank를 돌면서 min보다 면접 순위가 높으면 합격
    for i in range(1, len(rank)):
        if rank[i][1] < min:
            cnt += 1
            min = rank[i][1]
    
    print(cnt)
