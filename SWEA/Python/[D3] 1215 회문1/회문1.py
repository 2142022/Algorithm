#10개의 테스트케이스
for k in range(10):
    
    #회문의 길이
    length = int(input())

    #8X8 2차원 배열
    arr1 = [[col for col in input()] for row in range(8)]
    
    #회문의 개수
    cnt = 0

    #행마다 회문의 개수 구하여 더하기
    for i in range(8):
        for j in range(9-length):
            tmp1 = arr1[i][j:j+length]
            
            #tmp2는 tmp1을 뒤집은 리스트
            tmp2 = arr1[i][-9+j+length:-9+j:-1]

            #tmp1과 tmp1을 뒤집은 tmp2가 같다면 회문
            if tmp1 == tmp2:
                cnt += 1

    #arr1의 행과 열을 바꾼 2차원 리스트 (일단 0으로 초기화)
    arr2 = [[0 for col in range(8)] for row in range(8)]

    for i in range(8):
        for j in range(8):
            arr2[i][j] = arr1[j][i]
    
    #행마다 회문의 개수 구하여 더하기 (즉, 원래 행렬의 열을 기준으로)
    for i in range(8):
        for j in range(9-length):
            
            tmp1 = arr2[i][j:j+length]
            tmp2 = arr2[i][-9+j+length:-9+j:-1]
            
            if tmp1 == tmp2:
                cnt += 1

    print('#' + str(k+1) + ' ' + str(cnt))
