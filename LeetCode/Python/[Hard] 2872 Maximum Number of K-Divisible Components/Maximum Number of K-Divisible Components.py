class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # 노드가 1개인 경우
        if n == 1:
            return 1

        # 각 노드에서 연결된 노드
        connect = defaultdict(list)
        # 각 노드에서 연결된 노드의 개수
        connect_cnt = defaultdict(int)
        for a, b in edges:
            connect[a].append(b)
            connect[b].append(a)
            connect_cnt[a] += 1
            connect_cnt[b] += 1

        # k로 나누어떨어지는 합을 가진 부분의 개수
        cnt = 0

        # 연결된 간선이 1개인 노드를 담은 큐
        q = deque()
        for node in connect:
            if connect_cnt[node] == 1:
                q.append(node)
                connect_cnt[node] -= 1

        # 방문 체크
        visit = 0

        # 큐 탐색
        while q:
            # 같은 레벨에서 넣은 노드 탐색
            # 두 개의 노드에서 다음으로 가는 노드가 동일할 수 있기 때문
            for _ in range(len(q)):
                # 현재 노드
                node = q.popleft()

                # 방문 체크
                if visit & (1 << node):
                    continue
                visit += (1 << node)

                # 현재 노드까지의 value가 k의 배수라면 cnt 갱신
                if values[node] % k == 0:
                    cnt += 1

                # 연결된 노드 탐색
                for i in connect[node]:
                    # 현재 노드까지의 value가 k의 배수가 아니라면 현재 노드까지의 합을 다음 노드에 추가하기
                    if values[node] % k != 0:
                        values[i] += values[node]

                    # 연결 간선 삭제
                    connect_cnt[i] -= 1

                    # 연결된 노드의 개수가 1개라면 큐에 추가
                    if connect_cnt[i] == 1:
                        connect_cnt[i] -= 1
                        q.append(i)

        return cnt