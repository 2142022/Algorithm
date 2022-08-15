def plant(num):
    #총 가격(출력할 값)
    global price

    #한번심을 때마다 가격 더하기
    global result

    #꽃 3개를 모두 심었으면 return
    if (num == 4):
        price = min(result, price)
        return 
    
    for i in range(1, N-1):
        for j in range(1, N-1):
            if flag[i][j] == 0 and flag[i-1][j] == 0 and flag[i+1][j] == 0 and flag[i][j-1] == 0 and flag[i][j+1] == 0:
                flag[i][j] = 1
                flag[i-1][j] = 1
                flag[i+1][j] = 1
                flag[i][j-1] = 1
                flag[i][j+1] = 1
                result = result + arr[i][j] + arr[i-1][j] + arr[i+1][j] + arr[i][j-1] + arr[i][j+1]

                #재귀함수로 3번 심기
                plant(num+1)

                #다음 재귀를 위해 초기화
                flag[i][j] = 0
                flag[i-1][j] = 0
                flag[i+1][j] = 0
                flag[i][j-1] = 0
                flag[i][j+1] = 0
                result = result - arr[i][j] - arr[i-1][j] - arr[i+1][j] - arr[i][j-1] - arr[i][j+1]


N = int(input())

#화단 가격 입력받기
arr = [list(map(int, input().split())) for n in range(N)]

#꽃이 심어졌으면 1, 아니면 0
flag = [[0]*N for n in range(N)]

#최대 20000이므로 20000으로 초기화
price = 20000
result = 0

#꽃 심기
plant(1)

print(price)
