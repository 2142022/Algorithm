# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        # DFS로 연결할 수 있는 최대 간선 수 구하기
        # tree: 현재 탐색할 이진 트리
        # parent: 부모 노드의 번호
        def dfs(tree, parent):
            global max_cnt

            # 현재 노드의 번호
            num = tree.val

            # 왼쪽, 오른쪽 자식 트리에서 연결할 수 있는 간선 수
            left = right = 0
            if tree.left:
                left = dfs(tree.left, num)
            if tree.right:
                right = dfs(tree.right, num)

            # 연결할 수 있는 최대 간선 수 갱신
            max_cnt = max(max_cnt, left + right)

            # 부모 노드와 같다면 간선 수 추가
            if num == parent:
                return 1 + max(left, right)
            # 부모 노드와 다르다면 간선 수 0
            else:
                return 0

        #################################################################

        # root가 노드가 없는 빈 트리라면 바로 끝내기
        if not root:
            return 0

        # 연결할 수 있는 최대 간선 수
        global max_cnt
        max_cnt = 0

        # DFS로 최대 간선 수 구하기
        dfs(root, -1)

        return max_cnt