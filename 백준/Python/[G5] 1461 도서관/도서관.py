def solve(arr, M):
    # 내림차순 정렬
    arr.sort(reverse = True)

    #걸음 수
    step = 0

    for i in range(0,len(arr),M):
        step += arr[i]

    #돌아오는 걸음 수도 세야하므로 X2
    return step * 2

#총 책의 개수와 한 번에 들 수 있는 책의 개수
N, M = map(int, input().split())

#책의 위치 입력받기(arr1은 음수, arr2는 양수)
arr = list(map(int, input().split()))

#비어있는 경우 대비하여 0넣기
arr1 = [0]
arr2 = [0]

for i in arr:
    if (i < 0):
        arr1.append(i * (-1))
    else:
        arr2.append(i)

#걸음 수 더하기 (마지막에는 안 돌아와도 되므로 최대값은 빼기)
print(solve(arr1, M) + solve(arr2, M) - max(max(arr1), max(arr2)))
