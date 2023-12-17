class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        # DFS로 각 노드의 자손 노드 개수 구하기 
        def dfs(node):
            # 연결된 노드 개수
            cnt = 1
            
            # 자식 노드
            for c in children[node]:
                # 자식 노드에 연결되어 있는 노드 개수
                num = dfs(c)

                # 연결 노드 개수 증가
                cnt += num

                # 현재 노드를 제거했을 경우의 점수 증가
                score[node] *= num

            # 현재 노드가 루트 노드가 아닌 경우, 연결되지 않은 남은 노드의 개수(연결된 상위 노드의 점수) 곱하기
            if node:
                score[node] *= (N - cnt)

            return cnt

        #############################################################################################################

        # 노드 개수
        N = len(parents)

        # 자식 노드
        children = defaultdict(list)
        for c, p in enumerate(parents):
            children[p].append(c)

        # 각 노드를 제거했을 때의 점수
        score = [1] * N
        
        # 각 노드의 자손 노드 개수 구하기
        dfs(0)

        return score.count(max(score))

