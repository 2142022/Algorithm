# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # 재귀를 통해 도둑질 할 수 있는 최대값 구하기
        def get_amount(tree):
            # 현재 집
            node = tree.val

            # 자식 트리에서 구할 수 있는 최대값
            # l1, r1: 왼쪽, 오른쪽 각각의 자식 트리에서 자식 노드를 포함하지 않는 경우의 최대값
            # l2, r2: 왼쪽, 오른쪽 각각의 자식 트리에서 자식 노드를 포함하는 경우의 최대값
            l1 = l2 = r1 = r2 = 0
            if tree.left:
                l1, l2 = get_amount(tree.left)
            if tree.right:
                r1, r2 = get_amount(tree.right)

            # 현재 집을 도둑질하지 않았을 때의 값과 도둑질했을 때의 값 리턴
            return max(l1, l2) + max(r1, r2), l1 + r1 + node

        return max(get_amount(root))