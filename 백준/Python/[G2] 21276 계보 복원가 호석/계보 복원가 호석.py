from collections import defaultdict
import sys
input = sys.stdin.readline

# X의 시조 찾기
def find_root(X):
    if root[X] != X:
        root[X] = find_root(root[X])
    return root[X]

################################################

# 석호촌에 살고 있는 사람 수
N = int(input())

# 사람들의 이름
names = list(input().rstrip().split(' '))
# 사전순으로 정렬
names.sort()

# 사람들의 시조
root = defaultdict(str)
# 사람들의 조상 수
cnt = defaultdict(int)
for name in names:
    root[name] = name
    cnt[name] = 0

# 사람들의 자손
children = defaultdict(list)

# 계보 정보 개수
M = int(input())

# 계보 정보 탐색
for _ in range(M):
    # X의 조상 Y
    X, Y = input().rstrip().split(' ')

    # X의 조상 수 갱신
    cnt[X] += 1

    # X의 시조를 Y의 시조로 갱신
    root[X] = root[Y]

    # Y의 자손 갱신
    children[Y].append(X)

# 시조 이름
root_names_set = set()
for name in names:
    rn = find_root(name)
    if rn not in root_names_set:
        root_names_set.add(rn)

# 시조 이름 사전순 정렬
root_names = sorted(list(root_names_set))

# 시조 수 및 시조 이름 출력
print(len(root_names))
print(*root_names)

# 이름, 자식 수, 자식 이름 출력
for name1 in names:
    print(name1, end = ' ')

    # 자식 이름
    children_names = []
    for name2 in sorted(children[name1]):
        # 자손 중 조상 수의 차이가 1이면 자식
        if cnt[name1] + 1 == cnt[name2]:
            children_names.append(name2)

    # 자식이 있다면 이름 출력
    if len(children_names):
        print(len(children_names), *children_names)
    else:
        print(0)