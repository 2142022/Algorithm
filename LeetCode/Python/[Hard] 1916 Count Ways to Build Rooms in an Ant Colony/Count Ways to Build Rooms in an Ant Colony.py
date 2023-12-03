class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        # 자식 노드의 개수와 탐색 경우의 수
        def find(x):
            # 마지막 노드인 경우
            if not children[x]:
                return 1, 1

            # 자식 노드(자손 노드 포함)의 개수, 탐색 경우의 수
            c, r = 0, 1
            
            # 자식 노드 탐색
            for nx in children[x]:
                nc, nr = find(nx)
                c += nc

                # 탐색 경우의 수
                # = (현재 노드 x를 루트로 하는 서브 트리의 수)
                #   * (특정 자식 노드 선택)
                #   * (특정 자식 노드를 루트로 하는 서브 트리의 수)
                r = (r * comb(c, nc) * nr) % (10 ** 9 + 7)

            # c는 현재 노드까지 포함하기 위해 +1
            return c + 1, r

        ###########################################################################

        # 자식 노드
        children = defaultdict(list)
        for i in range(1, len(prevRoom)):
            children[prevRoom[i]].append(i)

        return find(0)[1]
