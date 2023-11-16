import sys
sys.setrecursionlimit(10000)

# 노드 
class Node:
    def __init__(self, info):
        self.val = info[2]
        self.pos = info[:2]
        self.left = self.right = None
        
###########################################################################

# 자식 노드 연결하기
def connect(parent, info):
    # 상위 노드보다 왼쪽에 있는 경우
    if parent.pos[0] > info[0]:
        # 이미 자식 노드가 있는 경우, 재귀를 통해 마지막 노드에 연결하기
        if parent.left:
            connect(parent.left, info)
        else:
            parent.left = Node(info)
    # 상위 노드보다 오른쪽에 있는 경우
    else:
        # 이미 자식 노드가 있는 경우, 재귀를 통해 마지막 노드에 연결하기
        if parent.right:
            connect(parent.right, info)
        else:
            parent.right = Node(info)
            
###########################################################################
            
# 전위 순회
def preorder(node):
    result = [node.val]
    if node.left:
        result += preorder(node.left)
    if node.right:
        result += preorder(node.right)
    return result

###########################################################################

# 후위 순회
def postorder(node):
    result = []
    if node.left:
        result += postorder(node.left)
    if node.right:
        result += postorder(node.right)
    result.append(node.val)
    return result
    
###########################################################################
       
def solution(nodeinfo):
    # nodeinfo에 노드 번호 추가
    for i in range(1, len(nodeinfo) + 1):
        nodeinfo[i - 1].append(i)
        
    # nodeinfo를 루트 노드부터 정렬
    nodeinfo.sort(key = lambda x : (-x[1], x[0]))
    
    # 이진 트리 만들기
    tree = Node(nodeinfo[0])
    for info in nodeinfo[1:]:
        connect(tree, info)
    
    # 전위 순회, 후위 순회 결과 반환
    return [preorder(tree), postorder(tree)]