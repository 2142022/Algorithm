#10번 반복
for i in range(10):

    length = int(input())                   #테스트 케이스 길이
    arr = list(map(int,input().split()))    #공백을 기준으로 int형으로 입력받고 리스트로 만듦
    result = 0

    #앞, 뒤 2칸씩 0이므로 range(2,length-2)
    for j in range(2,length-2):

        #자기 자신을 기준으로 앞뒤 2칸씩 슬라이싱
        tmp = arr[j-2:j+3]

        #자시 자신이 최대값이면 조망권 확보
        if (max(tmp) == arr[j]):
            #조망권 세대 수는 (최대값 - 다음으로큰 수)
            tmp.sort()
            result = result + tmp[4] - tmp[3]

    print('#' + str(i+1) + ' ' + str(result))
