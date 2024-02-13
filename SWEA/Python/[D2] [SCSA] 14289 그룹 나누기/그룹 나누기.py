# x가 포함된 조의 대표자(가장 작은 번호) 찾기
def find(x):
    if min_idx[x] != x:
        min_idx[x] = find(min_idx[x])
    return min_idx[x]

#######################################################

# 두 사람을 한 조로 묶기
def connect(a, b):
    # 두 사람의 조
    ga, gb = find(a), find(b)

    # 이미 두 사람이 같은 조라면 패스
    if ga == gb:
        return

    # 연결하기 (더 작은 번호로 저장)
    if ga < gb:
        min_idx[gb] = ga
    else:
        min_idx[ga] = gb

#######################################################

# 테스트 케이스
for T in range(1, int(input()) + 1):
    # 사람 수, 신청 수
    N, M = map(int, input().split())

    # 조마다 가장 작은 사람의 번호
    min_idx = [i for i in range(N + 1)]

    # 신청서
    submit = list(map(int, input().split()))

    # 두 사람을 한 조로 묶기
    for i in range(M):
        # 두 사람
        a, b = submit[2 * i], submit[2 * i + 1]

        # 연결하기
        connect(a, b)

    # 모든 사람의 대표자 갱신
    for i in range(1, N + 1):
        find(i)

    # 0번은 없으므로 -1
    print(f'#{T} {len(set(min_idx)) - 1}')