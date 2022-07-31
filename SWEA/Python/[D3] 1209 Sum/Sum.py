#10개의 테스트케이스
for k in range(10):

    #테스트케이스 번호 입력받기
    testcase = int(input())

    #100X100 2차원 리스트 입력받기
    arr = [[int(col) for col in input().split()] for row in range(100)]

    maxsum = 0

    #한 행의 합을 구하고 max값과 비교하기
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += arr[i][j]
        maxsum = max(maxsum, sum)

    #한 열의 합을 구하고 max값과 비교하기
    for j in range(100):
        sum = 0
        for i in range(100):
            sum += arr[i][j]
        maxsum = max(maxsum, sum)

    #좌측 상단에서 우측 하단으로 가는 대각선의 합 구하기
    sum = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                sum += arr[i][j]
    maxsum = max(maxsum, sum)

    #우측 상단에서 좌측 하단으로 가는 대각선의 합 구하기
    sum = 0
    for i in range(100):
        for j in range(100):
            if i + j == 198:
                sum += arr[i][j]
    maxsum = max(maxsum, sum)

    print('#' + str(testcase) + ' ' + str(maxsum))
