from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

# 노드 정의
class Node:
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right

####################################################################

# 중위 순회를 통해 마지막 노드 찾기
# idx: 탐색 노드
def get_end(idx):
    global end

    # 현재 노드
    node = nodes[idx]

    # 왼쪽 자식 노드 탐색
    if node.left != -1:
        get_end(node.left)

    # 현재 노드를 마지막 노드로 저장
    end = idx

    # 오른쪽 자식 노드 탐색
    if node.right != -1:
        get_end(node.right)

####################################################################

# DFS로 노드 탐색
# idx: 탐색 노드
def dfs(idx):
    global N, cnt, end

    # 현재 노드
    node = nodes[idx]

    # 왼쪽 자식 노드 방문
    if node.left != -1:
        cnt += 1
        dfs(node.left)

    # 모든 노드 탐색 완료
    if idx == end:
        print(cnt)
        exit()

    # 오른쪽 자식 노드 방문
    if node.right != -1:
        cnt += 1
        dfs(node.right)

    # 아직 탐색이 완료되지 않은 경우 부모 노드로 이동
    cnt += 1

####################################################################

# 노드 개수
N = int(input())

# 노드 연결
nodes = defaultdict(Node)
for _ in range(N):
    # 현재 노드, 왼쪽 자식 노드, 오른쪽 자식 노드
    a, b, c = map(int, input().split())
    nodes[a] = Node(a, b, c)

# 이동 횟수
cnt = 0

# 중위 순회를 통해 마지막 노드 찾기
end = 1
get_end(1)

# 노드 탐색
dfs(1)


