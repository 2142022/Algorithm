import sys
input = sys.stdin.readline

# 2부터 N까지의 정수에서 K번째로 지우는 수 구하기
N, K = map(int, input().split())

# 0부터 N까지의 정수가 삭제되었으면 True, 아직 삭제되지 않았다면 False
delete = [False] * (N + 1)

# K번째로 지우는 수
result = 0

# 2의 배수 지우기 -> 3의 배수 지우기 -> 5의 배수 지우기 ...
for i in range(2, N + 1):
    # i가 삭제되었다면 넘어가기
    if delete[i] == True:
        continue

    # 현재의 수의 배수들(현재의 수 * j) 중 아직 지워지지 않은 수 지우기
    j = 1
    while i * j <= N:
        # 아직 지워지지 않았다면 지우기
        if delete[i * j] == False:
            delete[i * j] = True

            # 정수를 지울 때마다 K도 하나씩 감소
            K -= 1

            # K가 0이 되었다면 K번째로 지운 수는 i * j
            if K == 0:
                result = i * j
                print(result)
                break

        j += 1

    # result가 0이 아니라면 끝내기
    if result != 0:
        break