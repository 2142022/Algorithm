import sys
input = sys.stdin.readline

# 집합
S = set()

# 연산
for _ in range(int(input())):
    # 수행할 연산과 그 값
    op = input().split()
    if op[0] == 'add':
        S.add(op[1])
    elif op[0] == 'remove':
        if op[1] in S:
            S.remove(op[1])
    elif op[0] == 'check':
        print(int(op[1] in S))
    elif op[0] == 'toggle':
        if op[1] in S:
            S.remove(op[1])
        else:
            S.add(op[1])
    elif op[0] == 'all':
        S = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'}
    elif op[0] == 'empty':
        S.clear()
