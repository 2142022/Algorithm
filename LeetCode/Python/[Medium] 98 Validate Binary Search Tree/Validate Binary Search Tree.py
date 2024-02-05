# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # 재귀를 통해서 서브 트리가 BST인지 확인
        def isBST(root, min_val = -sys.maxsize, max_val = sys.maxsize):
            
            # 루트 노드가 없는 경우 -> 이전 노드가 마지막 노드인 경우
            if root == None:
                return True
            
            # 현재 노드가 범위 내에 없다면 이진 탐색 트리X
            if not (min_val < root.val < max_val):
                return False
            
            # 왼쪽 자식 노드의 서브 트리와 오른쪽 자식 노드의 서브 트리 확인
            return isBST(root.left, min_val, root.val) & isBST(root.right, root.val, max_val)
        
        return isBST(root)