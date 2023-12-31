import sys
input = sys.stdin.readline

# 노드
class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None

#################################################

# 테스트케이스 수
T = int(input())
for _ in range(T):
    # 노드 수
    N = int(input())

    # 노드 생성 (1 ~ N)
    nodes = [0]
    for i in range(1, N + 1):
        nodes.append(Node(i))

    # 간선 정보 입력받기
    for _ in range(N - 1):
        A, B = map(int, input().split())
        nodes[B].parent = nodes[A]

    # 공통 조상을 구할 두 노드
    x, y = map(int, input().split())

    # x의 모든 조상
    ancestor = [x]
    node = nodes[x]
    while True:
        if node.parent:
            num = node.parent.val
            ancestor.append(num)
            node = nodes[num]
        else:
            break

    # y의 조상 찾기
    while True:
        # 가장 가까운 공통 조상을 찾은 경우
        if y in ancestor:
            print(y)
            break

        y = nodes[y].parent.val