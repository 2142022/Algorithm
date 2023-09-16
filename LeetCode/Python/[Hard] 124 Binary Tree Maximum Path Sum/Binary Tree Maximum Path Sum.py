# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 현재까지의 최대 경로 합 반환
        # tree: 현재 트리, s: 현재까지 연결된 경로 합
        def dfs(tree):
            global max_sum

            # 현재 노드
            n = tree.val

            # 자식 트리의 최대 경로 합
            left = right = 0
            if tree.left:
                left = dfs(tree.left)
            if tree.right:
                right = dfs(tree.right)

            max_sum = max(max_sum, n + left + right)

            # 왼쪽 자식 트리와 오른쪽 자식 트리 중 큰 값 반환
            m = max(n + left, n + right)
            if m > 0:
                return m
            else:
                return 0

        ###########################################################

        # 최대 경로 합
        global max_sum
        max_sum = root.val

        # DFS로 최대 경로 합 구하기
        dfs(root)

        return max_sum