class Kruskal:
    # 부모 리스트 및 MST의 가중치 합 초기화
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.weight = 0

    # 부모 노드 찾기
    def find_parent(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_parent(self.parent[x])
        return self.parent[x]

    # 부모 노드 바꾸기
    def union_parent(self, a, b):
        self.parent[b] = self.parent[a]

    # MST의 가중치 합 구하기
    def get_weight(self, edges):
        for i, a, b, w in edges:
            pa = self.find_parent(a)
            pb = self.find_parent(b)
            # 사이클이 발생하지 않는다면 연결하기
            if pa != pb:
                self.union_parent(pa, pb)
                self.weight += w
        return self.weight


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # 원래 인덱스를 포함하도록 간선 정보 갱신
        edges = [[i] + e for i, e in enumerate(edges)]
        # 간선의 가중치 기준으로 오름차순 정렬
        edges.sort(key=lambda x: x[3])

        # MST의 가중치
        mst = Kruskal(n)
        mst_weight = mst.get_weight(edges)

        # 모든 MST에 포함되는 간선의 인덱스
        critical = []
        # 모든 MST는 아니지만 1개 이상의 MST에 포함되는 간선의 인덱스
        pseudo_critical = []

        # 간선 하나씩 확인
        for i in range(len(edges)):
            # 두 노드 a, b를 연결하는 간선의 가중치 w
            # idx: 간선의 원래 인덱스
            idx, a, b, w = edges[i]

            # 현재 간선을 제외한 간선들
            remove_edge = edges[:i] + edges[i + 1:]

            # 현재 간선을 무조건 포함하는 MST
            contain = Kruskal(n)
            contain.union_parent(a, b)
            contain_weight = contain.get_weight(remove_edge) + w

            # 현재 간선을 포함한 MST의 가중치 합이 기존 MST의 가중치 합보다 크다면 MST가 될 수 없으므로 패스
            if contain_weight != mst_weight:
                continue

            # 현재 간선을 포함하지 않는 MST
            remove = Kruskal(n)
            remove_weight = remove.get_weight(remove_edge)

            # 현재 간선을 포함했을 때의 가중치 합은 MST의 가중치 합과 동일한 상태
            # 따라서, 현재 간선을 포함했을 때와 포함하지 않았을 때의 가중치 합이 같지 않다면
            # 현재 간선은 모든 MST에 포함되어 있음
            if contain_weight != remove_weight:
                critical.append(idx)
            else:
                pseudo_critical.append(idx)

        return [critical, pseudo_critical]