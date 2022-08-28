# 전위 순회
def preorder(c):
    print(c, end = '')

    # 자식 노드
    for i in range(N):
        if data[i][0] == c:
            # 왼쪽 자식 노드
            if data[i][1] != '.':
                preorder(data[i][1])
            # 오른쪽 자식 노드
            if data[i][2] != '.':
                preorder(data[i][2])

# 중위 순회
def inorder(c):
    # 왼쪽 자식 노드
    for i in range(N):
        if data[i][0] == c:
            if data[i][1] != '.':
                inorder(data[i][1])
                break

    print(c, end = '')

    #오른쪽 자식 노드
    for i in range(N):
        if data[i][0] == c:
            if data[i][2] != '.':
                inorder(data[i][2])
                break

# 후위 순회
def postorder(c):
    #자식 노드
    for i in range(N):
        if data[i][0] == c:
            # 왼쪽 자식 노드
            if data[i][1] != '.':
                postorder(data[i][1])
            #오른쪽 자식 노드
            if data[i][2] != '.':
                postorder(data[i][2])

    print(c, end = '')
           
import sys
input = sys.stdin.readline

# 노드의 개수
N = int(input())

# 노드 정보 입력
data = [0] * N
for i in range(N):
    data[i] = list(input().split())

preorder('A')
print()
inorder('A')
print()
postorder('A')
