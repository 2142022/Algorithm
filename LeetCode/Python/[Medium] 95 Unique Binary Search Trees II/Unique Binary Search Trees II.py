# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int):
        # start부터 end까지 연결하기
        def connect(start, end):
            # 더 이상 연결할 노드가 없는 경우
            if start > end:
                return [None]
            
            # 가능한 모든 트리
            trees = []
            for i in range(start, end + 1):
                # 현재 노드보다 작은 숫자를 이은 트리
                left = connect(start, i - 1)
                # 현재 노드보다 큰 숫자를 이은 트리
                right = connect(i + 1, end)
                
                # 두 트리의 원소를 하나씩 잇기
                for l in left:
                    for r in right:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        trees.append(node)
            
            return trees
        
        return connect(1, n)