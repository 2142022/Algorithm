# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # DFS로 targetSum 찾기
        # tree: 현재 트리
        # prefix_sum: 현재까지 지나온 노드들의 누적합 
        def dfs(tree, prefix_sum):
            global cnt

            # 현재 노드
            node = tree.val

            # 누적합 갱신
            for i in range(len(prefix_sum)):
                prefix_sum[i] += node
                # targetSum이라면 cnt 갱신
                if prefix_sum[i] == targetSum:
                    cnt += 1

            # 현재 노드만으로 targetSum이라면 cnt 갱신
            if node == targetSum:
                cnt += 1

            # 자식 노드 탐색
            if tree.left:
                dfs(tree.left, prefix_sum + [node])
            if tree.right:
                dfs(tree.right, prefix_sum + [node])

        ##########################################################

        # root가 []라면 0 리턴
        if not root:
            return 0

        # targetSum을 만들 수 있는 경로 개수
        global cnt
        cnt = 0

        # DFS로 targetSum 찾기
        dfs(root, [])

        return cnt