from collections import deque

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    arr = deque(list(map(int, input().split())))
    cnt = 1                             # 출력 횟
        
    while True:
        if arr[0] == max(arr):          # 맨 앞 문서의 중요도가 가장 클 때
            if M == 0:                  # 궁금한 문서가 맨 앞에 있을 때
                print(cnt)
                break
            else:                       # 궁금한 문서가 뒤에 있을 때
                arr.popleft()           # 맨 앞 문서 pop
                cnt += 1
                M -= 1
        else:                           # 중요도가 가장 큰 원소가 뒤에 있을 때
            if M == 0:                  # 궁금한 문서가 맨 앞에 있을 때
                arr.rotate(-1)          # 왼쪽으로 한 칸씩 이동
                M = len(arr) - 1
            else:                       # 궁금한 문서가 뒤에 있을 때
                arr.rotate(-1)
                M -= 1
