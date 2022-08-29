import sys
input = sys.stdin.readline

# 여러 테스트케이스
t = 1
while True:
    # 입력받기
    tree = []

    # 마지막 테스트케이스인지 확인
    final = 0

    # 0 0이 나올 때까지 반복해서 입력받기
    while True:
        tmp = list(map(int, input().split()))

        # 공백줄 건너뛰기
        if tmp == []:
            continue

        # 음수 2개가 나오면 끝내기
        elif tmp[-1] < 0 and tmp[-2] < 0:
            tree += tmp[:-4]
            final = 1
            break

        # 0 0이 나오면 0 0빼고 저장
        elif tmp[-1] == 0 and tmp[-2] == 0:
            tmp = tmp[:-2]
            tree += tmp
            break
            
        else:
            tree += tmp
        
        if tree[-1] == 0 and tree[-2] == 0:
            break

    # 음수 2개만 입력된 경우
    if tree == [] and final == 1:
        break
    # 0 0만 입력된 경우
    if tree == [] and final == 0:
        print('Case', t, 'is a tree.')
        t += 1
        continue

    # tree면 1, 아니면 0
    flag = 1

    # set으로 중복 원소 제거하여 노드 구하고 list로 바꾸기
    tmp = set(tree)
    node = list(tmp)

    # 자식 노드가 key, 부모 노드가 value인 딕셔너리 만들기
    dic = {}
    for i in range(len(tree)//2):
        # 이미 부모 노드가 있는 경우 트리 아님
        if tree[2 * i + 1] in dic.keys():
            flag = 0
            break
                      
        dic[tree[2*i + 1]] = tree[2*i]

    # 루트 노드 제외 모든 노드의 들어오는 간선의 수는 1개
    # 딕셔너리의 key의 개수 = 노드의 개수 - 1
    if len(node)-1 != len(dic.keys()):
        flag = 0

    # 순환하는 경우는 트리가 아님
    for i in dic.keys():
        value = dic[i]
        while True:
            if value == i:
                flag = 0
                break
            
            if value not in dic.keys():
                break
            else:
                value = dic[value]

    if flag == 1:
        print('Case', t, 'is a tree.')
    else:
        print('Case', t, 'is not a tree.')

    #마지막 테스트케이스인 경우
    if final == 1:
        break

    t += 1
