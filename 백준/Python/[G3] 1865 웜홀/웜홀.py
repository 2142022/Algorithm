from collections import defaultdict
import sys

input = sys.stdin.readline


# 시간이 줄어들면서 출발 위치 start로 돌아오는 것이 가능한 지 확인
def possible(start):
    # 출발 위치에서부터 각 위치까지 가는데 걸린 최단 시간
    time = [25000001] * (N + 1)
    time[start] = 0

    # 지점 수만큼 반복
    for cnt in range(N):
        # 모든 연결 확인
        for k, v in connect.items():
            # 현재 간선을 사용하는 경우 더 최단 시간인 경우 갱신
            nt = time[k[0]] + v
            if time[k[0]] != 25000001 and time[k[1]] > nt:
                time[k[1]] = nt
                visited[k[1]] = 1

                # 출발 지점까지의 거리가 줄어든 경우 끝내기
                if time[start] < 0:
                    return True

                # 계속 줄어드는 경우 끝내기
                if cnt == N - 1:
                    return True

    # 시간이 줄어들면서 출발 위치로 돌아오는 것이 불가능한 경우
    return False


#############################################################################

# 테스트 케이스
for _ in range(int(input())):
    # 지점 수, 도로 수, 웜홀 수
    N, M, T = map(int, input().split())

    # connect[(i, j)]: i와 j를 연결하는 도로나 웜홀 중 최소 시간
    connect = defaultdict(lambda: 25000001)
    for i in range(M + T):
        S, E, T = map(int, input().split())

        # 도로
        if i < M:
            connect[(S, E)] = connect[(E, S)] = min(connect[(S, E)], T)

        # 웜홀
        else:
            connect[(S, E)] = min(connect[(S, E)], -T)

    # 방문 체크
    visited = [0] * (N + 1)

    # 출발 지점
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = 1

            # 시간이 줄어들면서 출발 위치로 돌아오는 것이 가능한 경우
            if possible(i):
                print("YES")
                break

    # 시간이 줄어들면서 출발 위치로 돌아오는 것이 불가능한 경우
    else:
        print("NO")