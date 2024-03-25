import sys
input = sys.stdin.readline

# x폴더의 하위 폴더 중 볼 수 있는 목록 구하기
def get_folders(x):
    for child in children[x]:
        folders.append(child)

        # 토글이 펼쳐져 있는 경우
        if unfold[child]:
            get_folders(child)

#############################################################

# 폴더 수, 명령 수
N, Q = map(int, input().split())

# 하위 폴더, 상위 폴더
children = [list() for _ in range(N + 1)]
parent = [0] * (N + 1)
for i in range(1, N + 1):
    cnt, *child = map(int, input().split())
    children[i] = child
    for c in child:
        parent[c] = i

# 각 폴더의 펼쳐져 있는 여부
unfold = [0] * (N + 1)
unfold[1] = 1

# 현재 폴더
now = 1

# 명령
for _ in range(Q):
    # 명령, 이동 수 (이동 시에만 입력)
    command, *temp = input().split()
    if temp:
        cnt = int(temp[0])

    # 현재 볼 수 있는 폴더 목록
    folders = [1]
    get_folders(1)

    # 토글
    if command == 'toggle':
        unfold[folders[now]] ^= 1

    # 커서 이동
    else:
        # 목적지 (경계값을 벗어나지 않도록 설정)
        now = max(1, min(now + cnt, len(folders) - 1))
        print(folders[now])