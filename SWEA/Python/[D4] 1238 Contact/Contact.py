from collections import deque

# 테스트 케이스
for t in range(1, 11):
    # 데이터의 길이, 연락 시작점
    N, start = map(int, input().split())

    # 비상연락망
    contact = [list() for _ in range(101)]
    data = list(map(int, input().split()))
    for i in range(0, N, 2):
        p1, p2 = data[i], data[i + 1]
        contact[p1].append(p2)

    # 각 사람별 연락을 받게 되는 시간
    times = [-1] * 101
    times[start] = 0

    # 가장 나중에 연락을 받게 되는 시간, 그 중 가장 번호가 큰 사람
    max_time, max_idx = 0, start

    # 탐색하는 사람을 담은 큐
    q = deque([start])
    while q:
        # 탐색하는 사람과 연락을 받는 시간
        idx = q.popleft()
        time = times[idx]

        # 가장 마지막에 연락을 받는 사람 체크
        if time > max_time:
            max_time = time
            max_idx = idx
        elif time == max_time:
            max_idx = max(max_idx, idx)

        # 현재 사람이 연락할 수 있는 사람 큐에 담기
        for i in contact[idx]:
            if times[i] == -1:
                times[i] = time + 1
                q.append(i)

    print(f'#{t} {max_idx}')