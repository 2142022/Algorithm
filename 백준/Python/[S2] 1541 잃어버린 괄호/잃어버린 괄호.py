#'-' 기준으로 나누기
arr = list(input().split("-"))

#각 부분 계산하기
for i in range(len(arr)):
    #'+' 기준으로 나누기
    tmp = list(map(int, arr[i].split("+")))
    arr[i] = sum(tmp)

#결과값: arr[0] - 나머지
result = arr[0]
for i in range(1, len(arr)):
    result -= arr[i]

print(result)
